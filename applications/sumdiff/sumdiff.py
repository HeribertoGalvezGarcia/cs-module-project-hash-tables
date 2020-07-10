import itertools

from applications.cache import cache


"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


@cache
def f(x: int) -> int:
    return x * 4 + 6


def main() -> None:
    results = [(i, j, k, l) for i, j, k, l in itertools.product(q, repeat=4) if f(i) + f(j) == f(k) - f(l)]

    print('\n'.join(f'f({i}) + f({j}) = f({k}) - f({l})  {f(i)} + {f(j)} = {f(k)} - {f(l)}' for i, j, k, l in results))


if __name__ == '__main__':
    main()
