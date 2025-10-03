from tobin import *

def tokenize(program: str):
   lines = program.splitlines()
   return [line.split() for line in lines]

def open_file(path: str):
    with open(path, "r") as file:
        content = file.read()
    return content

def parse(program: str):
    tokens = tokenize(program)
    print(tokens)

"""
Model

Extension: .vasm

sum 2 numbers
    & = register
    only numbers = temporal number

    NOP
    ADD &save &num1 &num2
    SUB &save &num1 &num2
    IF cond DO ... ENDIF

"""
