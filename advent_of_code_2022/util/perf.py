from functools import wraps
from time import perf_counter


def perf(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__} took {(end - start):0.4f} seconds")
        return result

    return wrapper
