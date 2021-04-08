import re

# AA1
pattern = r"[A-Z][A-Z][0-9]"

if re.match(pattern, "AC9"):
    print("match found")
