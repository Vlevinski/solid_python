import time


def timer(func):
    """   A decorator to calculate how long a function runs.  """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {round(end - start, 4)} seconds to run!")
        return result

    return wrapper


class Timer:
    @timer
    def cycle(self, num):
        time.sleep(num)


@timer
def sleep(n):
    """  Sleep for n seconds  """
    time.sleep(n)


if __name__ == "__main__":
    # output like : "sleep took 5.0028 seconds to run!"
    sleep(5)
    t = Timer()
    t.cycle(5)
