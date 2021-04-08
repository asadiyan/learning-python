import re

pattern = r"^gr.y$"

""" '^' and '$' first one is for the starting point of pattern
and second one is for ending part of pattern
here they make a const for the start and end of pattern
now the example should start with g and the end should be with y """

if re.match(pattern, "gray"):
    print("match 1")
