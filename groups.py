import re

pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadeggsbread"):
    print("match found")

"""() and stars show that we han have none or
as many as we want eggs between 2 breads 0 to as many number
we want"""
