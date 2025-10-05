from compiler_error import VASMCompilationError
from tobin import empty32
from os import mkdir, path
from operations import Math, NOP

def write_bin(file, instruction: str, arg1: str, arg2: str, arg3: str): # Write a line of binary
    arg1 = dec_to_bin(arg1[1:])
    arg2 = dec_to_bin(arg2[1:])
    arg3 = dec_to_bin(arg3[1:])
    file.write("{}_{}_{}_{}\n".format(instructions[instruction], arg1, arg2, arg3))

empty32 = 32*"0" # A string of 32 zeroes

def write_bin(file, instruction: str, arg1: str, arg2: str, arg3: str): # Write a line of binary
    arg1 = dec_to_bin(arg1[1:])
    arg2 = dec_to_bin(arg2[1:])
    arg3 = dec_to_bin(arg3[1:])
    file.write("{}_{}_{}_{}\n".format(instructions[instruction], arg1, arg2, arg3))

def tokenize(program: str):
   lines = program.splitlines() # Split the file into lines
   return [word.split() for word in lines]  # Split the line into words or tokens

def open_file(path: str):
    with open(path, "r") as file: # Reads the file
        return file.read()

instruction_fns = {
    "NOP": NOP,
    "ADD": Math,
    "SUB": Math
}

def parse(program: str):

    code = open_file(program)
    tokens = tokenize(code)
    i: int = 0

    if not path.exists("./bin/"): # Create the bin folder if it doesnt exist
        mkdir("./bin")

    with open("./bin/a.vbin", "w+") as file:
        for i, line in enumerate(tokens): # Get the line number with i

            """

            Syntax Analizer

            """


            if not line or line[0][0] == "#": # Check if theres code or a comment
                continue

            if not instruction_fns.get(line[0]): 
                raise VASMCompilationError(
                    name="INVALID_INSTRUCTION",
                    expected=f"Invalid {line[0]} instruction.",
                    line=i
                )

            operation = line[0]
            args = line[1:]

            binary_line = instruction_fns[operation](operation, i, *args)
            file.write(binary_line)
