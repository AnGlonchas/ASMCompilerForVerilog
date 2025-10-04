
"""
Language Design:

Assembly extension: .vasm
Compiled bin extension: .vbin

    & -> register direction
    # -> number literals

    NOP
    ADD &save &num1 &num2
    SUB &save &num1 &num2
    IF cond DOIF ... ENDIF

"""

from tobin import *
from os import mkdir, path

def tokenize(program: str):
   lines = program.splitlines()
   return [word.split() for word in lines]

def open_file(path: str):
    with open(path, "r") as file:
        content = file.read()
    return content

def parse(program: str):
    code = open_file(program)
    tokens = tokenize(code)

    if not path.exists("./bin/"):
        mkdir("./bin")

    with open("./bin/a.vbin", "w+") as file:
        for line in tokens:
            if line:
                if line[0][0] == "#": # Comment
                    continue

                if len(line) == 1: # No arguments required (NOP)
                    file.write(f"{instructions[line[0]]}\n")

                else: # 3 Arguments required
                    file.write(f"{instructions[line[0]]}_{dec_to_bin(line[1][1:])}_{dec_to_bin(line[2])}_{dec_to_bin(line[3])}\n")

        print(file.read())
    #print(tokens)

