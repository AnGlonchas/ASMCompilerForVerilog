from dataclasses import dataclass
from compiler_error import VASMCompilationError
"""

& -> registers
# -> number literal

"""
BINARY = 0
FUNCTION = 1

empty32 = 32*"0" # A string of 32 zeroes

def tobin(numstr: str):
        num = int(numstr)
        if num == 0:
            return empty32
        elif num == 1:
            return (31*"0")+"1"
        else:
            numbin = ""
            while num > 0:
                module = num % 2
                num = num // 2
                numbin = str(module) + numbin
            #Put the rest of the zeroes
            return (32-len(numbin))*"0" + numbin

class Instruction:
    def __init__(self, opcode: str, args: list[str], line: int):
        self.opcode = opcode

        if not args:
            pass
        else:
            self.arg1, self.arg2, self.arg3 = [*args]

        self.line = line
        self.instructions =  {
            "NOP":  ("00000000", self.NOP), #No operations
            "ADD":  ("00000001", self.Math), #Add two numbers (&, #, #)
            "SUB":  ("00000010", self.Math),
            "IF":   ("00000011", self.Math),
            "MORE": ("00000100", self.Math),
            "LESS": ("00000101", self.Math),
            "ADDI": ("00000110", self.iMath),
            "TAG":  ("00000110", self.Math)
        }
        self.bin_opcode = self.instructions[self.opcode][BINARY]
        self.bin_line = self.instructions[self.opcode][FUNCTION]()

    def iMath(self) -> str:
        if self.arg1[0] != "&" or self.arg2[0] != "&":
            raise VASMCompilationError(
                name="EXPECTED_REG_ERR",
                line=line,
                expected="Expected a register as an argument."
            )

        if not (self.arg1 or self.arg2 or self.arg3):
            raise VASMCompilationError(
                name="INVALID_REG_ERR",
                line=line,
                expected="Expected 3 arguments."
            )

        return f"{self.bin_opcode}_{tobin(self.arg1[1:])}_{tobin(self.arg2[1:])}_{tobin(self.arg3)}\n"


    def Math(self) -> str:

        if self.arg1[0] != "&" or self.arg2[0] != "&" or self.arg3[0] != "&":
            raise VASMCompilationError(
                name="EXPECTED_REG_ERR",
                line=line,
                expected="Expected a register as an argument."
            )

        if not (self.arg1 or self.arg2 or self.arg3):
            raise VASMCompilationError(
                name="INVALID_REG_ERR",
                line=line,
                expected="Expected a register identificator."
            )

        return f"{self.bin_opcode}_{tobin(self.arg1[1:])}_{tobin(self.arg2[1:])}_{tobin(self.arg3[1:])}\n"

    def NOP(self) -> str:
        return f"{self.bin_opcode}_{empty32}_{empty32}_{empty32}\n"

    def convert(self) -> str:
        return self.bin_line




        

