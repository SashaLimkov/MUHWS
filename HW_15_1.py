def dec_fun(func):
    def wrapper(*args, **kwargs):
        print("I am decorator")
        func(*args, **kwargs)

    return wrapper


@dec_fun
def some_fun(name):
    print(f"Hello {name}")


if __name__ == '__main__':
    some_fun("Egor")
