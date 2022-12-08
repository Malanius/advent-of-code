from functools import wraps
from time import perf_counter_ns


def perf(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        end = perf_counter_ns()
        print(f"{func.__name__} took {(end - start)/1_000_000:0.4f} ms")
        return result

    return wrapper
