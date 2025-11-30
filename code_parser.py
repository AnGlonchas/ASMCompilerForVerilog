from compiler_error import VASMCompilationError
from tobin import Instruction
from os import mkdir, path
from core import *  

def parse(program: str) -> str:

    code = open_file(program).replace(",", "")
    tokens = tokenize(code)
    result = ""

    if not path.exists(BIN_PATH): # Create the bin folder if it doesnt exist
        mkdir(BIN_PATH)

    with open(BIN_PATH+"a.vbin", "w+") as file:
        for i, line in enumerate(tokens): # Get the line number with i

            """

            Syntax Analizer

            """

            if not line or line[0][0] == "#": # Check if theres code or a comment
                continue

            operation = line[0].upper()
            args = line[1:]
            instruction = Instruction(operation, args, i)
            bin_line = instruction.convert()

            if not bin_line:
                raise VASMCompilationError(
                    name="INVALID_INSTRUCTION",
                    expected=f"Invalid {operation} not found.",
                    linecontent=line,
                    line=i
                )

            file.write(bin_line)
            result += bin_line
    return result

def parseline(instruction: str) -> str:
    tokens = tokenize(instruction.replace(",", ""))
    result = ""
    for i, line in enumerate(tokens): # Get the line number with i
        """
        Syntax Analizer
        """
        if not line or line[0][0] == "#": # Check if theres code or a comment
            continue

        operation = line[0].upper()
        args = line[1:]
        instruction = Instruction(operation, args, i)
        bin_line = instruction.convert()

        if not bin_line:
            raise VASMCompilationError(
                name="INVALID_INSTRUCTION",
                expected=f"Invalid {operation} not found.",
                linecontent=line,
                line=i
            )
        result += bin_line
    return result

