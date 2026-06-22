def build_intro(name: str, age: str, school: str, major: str) -> str:
    intro = (
        f"Hello, my name is {name}.\n"
        f"I am {age} years old.\n"
        f"I study at {school}.\n"
        f"My major is {major}."
    )
    return intro


def main() -> None:
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    school = input("Please enter your school: ")
    major = input("Please enter your major: ")

    intro = build_intro(name, age, school, major)

    print()
    print("Generated Introduction:")
    print("-----------------------")
    print(intro)


if __name__ == "__main__":
    main()