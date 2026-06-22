from argparse import ArgumentParser
from pathlib import Path
from typing import TypedDict


class ScanResult(TypedDict):
    root: Path
    file_count: int
    directory_count: int
    total_size: int
    extension_counts: dict[str, int]


def format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    return f"{size_bytes / (1024 * 1024):.2f} MB"


def scan_directory(root: Path) -> ScanResult:
    file_count = 0
    directory_count = 0
    total_size = 0
    extension_counts: dict[str, int] = {}

    for path in root.rglob("*"):
        if ".git" in path.parts:
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
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()

    if not root.exists():
        raise FileNotFoundError(f"Path does not exist: {root}")

    if not root.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {root}")

    result = scan_directory(root)
    print_report(result)


if __name__ == "__main__":
    main()