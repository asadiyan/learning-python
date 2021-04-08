import re

pattern = r"gr.y"

if re.match(pattern, "gray"):
    print("match found")

"""here in pattern we have dot, so we can 
put any anything in the replace like in the example:
we added a to the dot place"""
