from tobin import *
from parser import *

print(f"{instructions["LESS"]}_{dec_to_bin("100")}")


asm = "SUM   &0 2 2\nLESS &0 2 2"

"""
line = asm.splitlines()
y = [word.split() for word in line]
"""

print(open_file("test.vasm"))

def main():
    parse("SUM   &0 2 2\nLESS &0 2 2")


if(__name__ == "__main__"):
    main()
