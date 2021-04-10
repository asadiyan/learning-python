def add(x):
    return x + 2


myList = [10, 20, 30, 40, 50]

result = list(map(add, myList))

# when we use lambda then we dont need the function add().
result = list(map(lambda x: x + 2, myList))

print(result)

prices = [100, 56, 28, 34, 50]


def discount(x):
    return x - (x * 10) / 100


print("prices without any dicount:\n" + str(prices))
print("""prices after adding 10% dicount:""")
print(list(map(discount, prices)))
