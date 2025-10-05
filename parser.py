from compiler_error import VASMCompilationError
from tobin import empty32
from os import mkdir, path
from core import BIN_PATH
from operations import *

def open_file(path: str):
    with open(path, "r") as file: # Reads the file
        return file.read()

def tokenize(program: str):
   lines = program.splitlines() # Split the file into lines
   return [word.split() for word in lines]  # Split the line into words or tokens

instruction_fns = {
    "NOP": NOP,
    "ADD": Math,
    "SUB": Math
}

def parse(program: str):

    code = open_file(program)
    tokens = tokenize(code)

    if not path.exists(BIN_PATH): # Create the bin folder if it doesnt exist
        mkdir(BIN_PATH)

    with open(BIN_PATH+"a.vbin", "w+") as file:
        for i, line in enumerate(tokens): # Get the line number with i

            """

            Syntax Analizer

            """


            if not line or line[0][0] == "#": # Check if theres code or a comment
                continue

            operation = line[0]
            args = line[1:]

            if not instruction_fns[operation]: # Checks if the instruction exist
                raise VASMCompilationError(
                    name="INVALID_INSTRUCTION",
                    expected=f"Invalid {operation} not found.",
                    line=i
                )


            binary_line = instruction_fns[operation](operation, i, *args)
            file.write(binary_line)
