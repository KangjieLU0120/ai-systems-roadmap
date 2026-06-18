def build_message(name: str) -> str:
    message = f"Hello, {name}!"
    return message


def main():
    name = input("Your name: ")
    greeting = build_message(name)
    print(greeting)


if __name__ == "__main__":
    main()