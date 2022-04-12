import time


def dec_fun(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        r = func(*args, *kwargs)
        f = time.time()
        print(f"Время выполнения - {s - f}")
        return r

    return wrapper


@dec_fun
def perim(side):
    p = side * 4
    return p


if __name__ == '__main__':
    print(perim(44))
