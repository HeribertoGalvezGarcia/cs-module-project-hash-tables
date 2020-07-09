with open('ciphertext.txt') as f:
    text = f.read()

frequency_order = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P',
                   'K', 'V', 'Q', 'J', 'X', 'Z']


def main() -> None:
    filtered_text = ''.join(filter('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.__contains__, text))

    count = {}

    for char in filtered_text:
        try:
            count[char] += 1
        except KeyError:
            count[char] = 1

    sorted_count = sorted(count, key=count.get, reverse=True)
    print(text.translate({ord(x): y for x, y in zip(sorted_count, frequency_order)}))


if __name__ == '__main__':
    main()
