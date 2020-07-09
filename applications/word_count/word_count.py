from typing import Dict


def word_count(s: str) -> Dict[str, int]:
    count = {}

    for word in s.translate({ord(c): '' for c in r'":;,.-+=/\|[]{}()*^&'}).lower().split():
        try:
            count[word] += 1
        except KeyError:
            count[word] = 1

    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
