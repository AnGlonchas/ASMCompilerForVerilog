from tobin import *


def open_file(path: str):
    with open(path, "r") as file:
        content = file.read()
    return content


def parse():
	pass    

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