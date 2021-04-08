import re

pattern = r"eggs"

if re.match(pattern, "brok;eggseggs;kni"):
    print("match found")
else:
    print("match not found")


"""because in the pattern we have at the first of it brok it will print:
match not found but if matchable pattern start with eggs and it doesn`t matter
ends with what we will get the match found """


if re.search(pattern, "bork;eggseggs;kni"):
    print("match found")
else:
    print("match not found")

if re.findall(pattern, "bork;eggseggs;kni"):
    print("match found")
else:
    print("match not found")

