from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(
            f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def wait_for(seconds):
    """
    Simple function that waits and returns f-string.
    """
    time.sleep(seconds)
    return f"Waited for {seconds} seconds"


def my_decorator(func, *args, **kwargs):
    def wrapper():
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper


def count(times):
    for i in range(times):
        print(f"count {i}")


wrapped_count = my_decorator(count, 10)

wrapped_count()

wait_for(5)
