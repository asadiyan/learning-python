class A:
    def a_method(self):
        print("this a method from A")


class B:
    def b_method(self):
        print("this a method from B")


class C(A, B):
    def c_method(self):
        print("this a method from C")


c_object = C()
c_object.a_method()
c_object.b_method()
c_object.c_method()
