class Myclass:
    __hiddenvariable = 0

    def add(self, increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)


object1 = Myclass()
object1.add(5)

# "__" this will make the Attribute unreachable from outside of
# class even we have object with the name of object1
# so if we type print(object1.__hiddenvariable) we will get 
# an error that will say class Myclass does not have Attribute
# in the name of __hiddenvariable!
