import time


def dec_get_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print(f"Время затраченное на выполнение функции - {stop - start}")
        return result

    return wrapper


@dec_get_time
def get_rectangle_S(a, b):
    time.sleep(2)
    return a * b


print(get_rectangle_S(10, 100))
