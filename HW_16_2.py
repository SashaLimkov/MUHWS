import time
import functools


class Test:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func()
        time.sleep(3)
        print("bye")
        return 0


@Test
def hello():
    print("Hello")


if __name__ == '__main__':
    hello()
