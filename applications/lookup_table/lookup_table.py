import math
import random

from applications.cache import cache


def slowfun_too_slow(x: int, y: int) -> int:
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


@cache
def slowfun(x: int, y: int) -> int:
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def main() -> None:
    # Do not modify below this line!
    for i in range(50000):
        x = random.randrange(2, 14)
        y = random.randrange(3, 6)
        print(f'{i}: {x},{y}: {slowfun(x, y)}')


if __name__ == '__main__':
    main()
