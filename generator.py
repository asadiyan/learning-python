def get_list():
    result = []
    i = 0
    while i < 10:
        print("im generating :" + str(i))
        result.append(i)
        i += 1
    return result


def get_generator():
    i = 0
    while i < 10:
        yield i
        print("im generating :" + str(i))
        i += 1


for x in get_list():
    print(x)


print("------------------------------------------------------")


for x in get_generator():
    print(x)
