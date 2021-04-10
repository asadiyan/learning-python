import re

pattern = r"eggs(bacon)*"

if re.match(pattern, "eggsbacon"):
    print("match found")

"""when we have star character in there that meanes:
the word or group of bacon:
can be in the pattern and it cant be it doesn`t matter at all,
just for bacon not esggs, eggs should be in the pattern"""
