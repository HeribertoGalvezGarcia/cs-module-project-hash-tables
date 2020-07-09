import functools
from typing import Any, Callable, TypeVar

T = TypeVar('T')


def cache(func: Callable[..., T]) -> Callable[..., T]:
    _cache = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> T:
        key = args

        try:
            value = _cache[key]
        except KeyError:
            _cache[key] = value = func(*args)
            return value
        else:
            return value

    wrapper.cache = _cache
    return wrapper
