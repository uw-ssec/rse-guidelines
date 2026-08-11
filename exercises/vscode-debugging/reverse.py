from typing import List, Optional


def reverse_in_place(s: List[str], start: int = 0, end: Optional[int] = None):
    if end is None:
        end = len(s)
    for i in range(0, (end - start) // 2):
        temp = s[i + start]
        s[i + start] = s[end - i - 1]
        s[end - i - 1] = temp


def reverse_each_word(s: List[str]):
    size = len(s)
    left = 0
    for i in range(size):
        if s[i] == " ":
            reverse_in_place(s, left, i)
            left = i + 1
    reverse_in_place(s, left, size)


def reverse_words(s: List[str]):
    reverse_in_place(s)
    reverse_each_word(s)


def tostr(s: List[str]):
    return "".join(s)


if __name__ == "__main__":
    s = "hello world"
    x = list(s)
    reverse_in_place(x)
    print(f"Reverse of '{s}' -> {tostr(x)}")

    x = list(s)
    reverse_each_word(x)
    print(f"Reverse each word of '{s}' -> {tostr(x)}")

    x = list(s)
    reverse_words(x)
    print(f"Reverse words of '{s}' -> {tostr(x)}")
