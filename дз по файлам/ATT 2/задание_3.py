class MyIter:
    def __init__(self, l):
        self.l = l
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.l) > self.i:
            elem = self.l[self.i]
            self.i += 1
            return elem
        else:
            raise StopIteration

some_iter = MyIter([1, 2, 3, 4, 5, 6])
print(next(some_iter))
print(next(some_iter))
print(next(some_iter))
print(next(some_iter))
print(next(some_iter))
print(next(some_iter))
print(next(some_iter))
