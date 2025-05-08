from typing import Callable, TypeVar, ParamSpec
from functools import wraps
import time

T = TypeVar("T")
P = ParamSpec("P")


def retry(
    max_attempts: int = 5,
    interval_in_seconds: int = 0,
) -> Callable[[Callable[P, T]], Callable[P, T | None]]:
    def inner_decorator(
        func: Callable[P, T],
    ) -> Callable[P, T | None]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T | None:
            for attempt in range(max_attempts - 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1}/{max_attempts} failed: {e}")
                    time.sleep(interval_in_seconds)
                    if attempt == max_attempts:
                        raise e

        return wrapper

    return inner_decorator
