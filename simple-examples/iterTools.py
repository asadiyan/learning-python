from itertools import count, accumulate, takewhile


# count example:

# for i in count(3):
#    print(i)
#
#   if i >= 20:
#       break


# accumulate example:

numbers = list(accumulate(range(8)))
print(numbers)
print(list(takewhile(lambda x: x <= 10, numbers)))
