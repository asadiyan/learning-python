def student_discount(price):
    price = price - (price * 10) / 100
    return price


def regular_dicount(newPrice):
    newPrice = newPrice - (newPrice * 5) / 100
    return newPrice


sellingPrice = 100

print(regular_dicount(student_discount(sellingPrice)))
