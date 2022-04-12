class TestList(list):
    def append(self, value):
        return self.pop()


new_list = TestList([1, 2, 3])
print(type(new_list))
new_list.append(2)
print(new_list)
# a = [1, 2, 3, 4, 5]
# print(a)
# a.append(5)
# print(a)
