from tobin import *
from os import mkdir, path

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

def parse(program: str):

    code = open_file(program)
    tokens = tokenize(code)

    if not path.exists("./bin/"): # Create the bin folder if it doesnt exist
        mkdir("./bin")

    with open("./bin/a.vbin", "w+") as file:
        for i, line in enumerate(tokens): # Get the line number with i

            """

            Syntax Analizer

            """


            if not line or line[0][0] == "#": # Check if theres code or a comment
                continue

            if len(line) == 1: # No arguments required (NOP)
                write_bin(file, line[0], empty32, empty32, empty32)

            elif len(line) == 4: # 4 Words required (1 Operation, 3 Arguments)
                write_bin(file, *line)

            else: # There are NOT 4 words in the line
                raise Exception(f"\n\nToo {"many" if len(line) > 3 else "little"} arguments\nLine: {i+1}\n")
