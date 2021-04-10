def factorial(x):
    if x == 0:
        print("zero is not acceptable")
    elif x == 1:
        return 1
    else:
        return x * (factorial(x - 1))


value = input("eneter a number: \n")
print(factorial(int(value)))

