class Data:
    def __init__(self):
        self.value = ""

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class Child(Data):
    name = Data()
    lastname = Data()
    age = Data()


person1 = Child
person1.name = "Вася"
person1.age = 13
person1.lastname = "sada"
print(person1.name)
print(person1.age)
print(person1.lastname)
