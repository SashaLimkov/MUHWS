class IterList:
    def __init__(self, l):
        self.l = l
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.l):
            index = self.i
            self.i += 1
            return self.l[index]
        else:
            raise StopIteration


a = IterList(["sdfsdf", 1, 2])
print(type(a))
print(next(a.__iter__()))
print(type(a))
print(next(a))
print(next(a))
print(next(a))
