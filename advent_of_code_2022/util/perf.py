from functools import wraps
from time import perf_counter_ns


def perf(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        end = perf_counter_ns()

        time_taken = (end - start) / 1_000_000
        took = f"{time_taken:0.4f} ms"
        if time_taken > 1_000:
            seconds = time_taken / 1_000
            took = f"{seconds:0.4f} s"
        if time_taken > 1_000 * 60:
            mins = time_taken / (1_000 * 60)
            took = f"{mins:0.4f} min"
        print(f"{func.__name__} took {took}")
        return result

    return wrapper
