with open('robin.txt') as f:
    text = f.read()


def main() -> None:
    words = {}
    sanitized_text = text.translate({ord(c): '' for c in r'":;,.-+=/\|[]{}()*^&'}).lower().split()
    longest_word = len(max(sanitized_text, key=len))

    for word in sanitized_text:
        try:
            words[word] += 1
        except KeyError:
            words[word] = 1

    print('\n'.join(f'{word: <{longest_word + 2}}{"#" * amount}'
                    for word, amount in sorted(words.items(), key=lambda x: (-x[1], x[0]))))


if __name__ == '__main__':
    main()
