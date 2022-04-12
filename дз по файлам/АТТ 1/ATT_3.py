class TestList(list):
    def append(self, value):
        for i in range(len(self)):
            self[i] **= value


new_list = TestList([1, 2, 3])
print(new_list)
new_list.append(2)
print(new_list)
