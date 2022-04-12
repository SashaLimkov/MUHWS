class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)
        return self.name

    def get_age(self):
        print(self.age)
        return self.age


class Student(Person):
    def __init__(self, name: str, age: int, school, grade: int):
        super().__init__(age, name)
        self.school = school
        self.grade = grade

    def get_school(self):
        print(self.school)
        return self.school

    def get_grade(self):
        print(self.grade)
        return self.grade


person = Person(name="Name",age= 19)
person.get_age()
student = Student("Мансур", 10, "5", 5)
# student.get_name()
student.get_age()
# student.get_school()
# student.get_grade()
