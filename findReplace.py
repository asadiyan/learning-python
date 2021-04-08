import re

string = "my name is abi, hi i am abi"

pattern = r"abi"
newstring = re.sub(pattern, "hamidreza", string)
print(newstring)
