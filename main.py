import sys
from findSchool import findSchool

s = """
Usage: python3 main.py [school code]
"""

if (len(sys.argv) == 1):
    print(s)
    exit()

print(findSchool(sys.argv[1]))
