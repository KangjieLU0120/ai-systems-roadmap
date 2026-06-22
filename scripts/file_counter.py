from argparse import ArgumentParser
from pathlib import Path
from typing import TypedDict


class ScanResult(TypedDict):
    root: Path
    file_count: int
    directory_count: int
    total_size: int
    extension_counts: dict[str, int]


DEFAULT_EXCLUDED_DIRS = {
    ".git",
    ".vscode",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}


def format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    return f"{size_bytes / (1024 * 1024):.2f} MB"


def should_skip_path(path: Path, include_hidden: bool) -> bool:
    if include_hidden:
        return False

    return any(part in DEFAULT_EXCLUDED_DIRS for part in path.parts)


def scan_directory(root: Path, include_hidden: bool = False) -> ScanResult:
    file_count = 0
    directory_count = 0
    total_size = 0
    extension_counts: dict[str, int] = {}

    for path in root.rglob("*"):
        if should_skip_path(path, include_hidden):
            continue

        if path.is_dir():
            directory_count += 1
            continue

        if path.is_file():
            file_count += 1
            total_size += path.stat().st_size

            extension = path.suffix.lower() or "[no extension]"
            extension_counts[extension] = extension_counts.get(extension, 0) + 1

    return {
        "root": root,
        "file_count": file_count,
        "directory_count": directory_count,
        "total_size": total_size,
        "extension_counts": extension_counts,
    }


def print_report(result: ScanResult) -> None:
    print(f"Scan root: {result['root']}")
    print(f"Files: {result['file_count']}")
    print(f"Directories: {result['directory_count']}")
    print(f"Total size: {format_size(result['total_size'])}")

    print("\nExtensions:")
    for extension, count in sorted(result["extension_counts"].items()):
        print(f"  {extension}: {count}")


def main() -> None:
    parser = ArgumentParser(description="Count files in a directory.")
    parser.add_argument("path", help="Directory path to scan")
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include hidden and cache directories such as .git and .venv",
    )
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()

    if not root.exists():
        raise FileNotFoundError(f"Path does not exist: {root}")

    if not root.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {root}")

    result = scan_directory(root, include_hidden=args.include_hidden)
    print_report(result)


if __name__ == "__main__":
    main()