class A:
    def a_method(self):
        print("this is a method of A")


class B(A):
    def b_method(self):
        print("this is a method of B")


class C(B):
    def c_method(self):
        print("this is a method of C")


c_object = C()
c_object.c_method()
c_object.b_method()
c_object.a_method()
