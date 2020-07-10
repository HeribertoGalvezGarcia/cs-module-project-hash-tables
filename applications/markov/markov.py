import random
import re


with open("input.txt") as f:
    words = f.read()

starting_re = re.compile(r'^"?[A-Z].+')


def main() -> None:
    follow_ups = {}
    split_words = words.split()

    for i, word in enumerate(split_words, 1):
        try:
            next_word = split_words[i]
        except IndexError:
            continue

        try:
            follow_ups[word].append(next_word)
        except KeyError:
            follow_ups[word] = [next_word]

    for _ in range(10):
        start_word = ''

        while not starting_re.match(start_word):
            start_word = random.choice(split_words)

        sentence = [start_word]

        while not sentence[-1].endswith(('.', '!', '?', '".', '"!', '"?')):
            sentence.append(random.choice(follow_ups[sentence[-1]]))

        print(' '.join(sentence))


if __name__ == '__main__':
    main()
