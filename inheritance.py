class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        self.name = input("enetr your name\n")
        self.age = input("eter your age\n")

    def put_data(self):
        print(self.name + "\n" + self.age)


class ScienceStudent(Student):

    def scince(self):
        print("this is scince method")


a = ScienceStudent("", "")
a.get_data()
