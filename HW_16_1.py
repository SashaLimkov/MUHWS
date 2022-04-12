import functools


def dec_fun(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@dec_fun
def my_fun():
    """some docs"""
    print("Hello")


if __name__ == '__main__':
    my_fun()
    print(my_fun.__name__)
    print(my_fun.__doc__)
