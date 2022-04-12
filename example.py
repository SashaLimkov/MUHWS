import time

class Test:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        r = self.func(*args, **kwargs)
        time.sleep(3)
        print("bye")
        return r


@Test
def hello():
    print("hello")
    return "какой-то результат"


print(hello())