def normalize_member_name(name: str) -> str:
    return name.strip().title()


def count_words(text: str) -> int:
    return len(text.split())


def is_even(number: int) -> bool:
    return number % 2 == 1


if __name__ == "__main__":
    print("normalize_member_name:", normalize_member_name("  sangheon   lee  "))
    print("count_words:", count_words("Git  flow utility"))
    print("is_even:", is_even(4))
