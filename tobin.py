from dataclasses import dataclass
from compiler_error import VASMCompilationError
"""

& -> registers
# -> number literal

"""
BINARY = 0
FUNCTION = 1
SPECIAL = 2

def empty(wordlength: int = 32):
    return wordlength*"0"

def tobin(numstr: str, wordlength: int = 32):
    try:
        num = int(numstr)
        res = format(num, f"0{wordlength}b")
        return res

    except VASMCompilationError:
        VASMCompilationError(
            name="INVALID_NUMBER_LITERAL",
            expected=f"",
            linecontent="",
            line=""
        )

class Instruction:
    def __init__(self, opcode: str, args: list[str], line: int):
        self.opcode = opcode

        if not args: pass
        if len(args) == 1: self.arg1 = args[0]
        if len(args) == 2: self.arg1, self.arg2 = args
        if len(args) == 3: self.arg1, self.arg2, self.arg3 = args

        self.line = line
        self.instructions =  {
            # R type syntax (&, &, &)
            "ADD":  ("000000", self.Math, "100000"),
            "SUB":  ("000000", self.Math, "100010"),
            "AND":  ("000000", self.Math, "100100"),
            "OR":   ("000000", self.Math, "100101"),
            "SLT":  ("000000", self.Math, "101010"),
            # I type syntax (&, &, #)
            "ADDI": ("001000", self.iMath),
            "ANDI": ("001100", self.iMath),
            "ORI":  ("001101", self.iMath),
            "XORI": ("001110", self.iMath),
            "SLTI": ("001010", self.iMath),
            "BEQ":  ("000100", self.iMath),
            "LW":   ("100011", self.iMath),
            "SW":   ("101011", self.iMath),
            # J type syntax (#)
            "J":    ("000010", self.Jump),
        }

        self.bin_opcode = self.instructions[self.opcode][BINARY]
        self.bin_line = self.instructions[self.opcode][FUNCTION]()

    def Jump(self) -> str:
        if self.arg1[0] != "#":
            raise VASMCompilationError(
                name="EXPECTED_REG_ERR",
                line=self.line,
                expected="Expected an immediate number as an argument (#)."
            )

        return f"{self.bin_opcode}_{tobin(self.arg1[1:], 26)}\n"

    def iMath(self) -> str:
        if self.arg1[0] != "&" or self.arg2[0] != "&":
            raise VASMCompilationError(
                name="EXPECTED_REG_ERR",
                line=self.line,
                expected="Expected a register as an argument."
            )
        if self.arg3[0] != "#":
            raise VASMCompilationError(
                name="EXPECTED_REG_ERR",
                line=self.line,
                expected="Expected an immediate number as an argument."
            )

        if not (self.arg1 or self.arg2 or self.arg3):
            raise VASMCompilationError(
                name="INVALID_REG_ERR",
                line=self.line,
                expected="Expected 3 arguments (&, &, #)."
            )
        return f"{self.bin_opcode}_{tobin(self.arg2[1:], 5)}_{tobin(self.arg1[1:], 5)}_{tobin(self.arg3[1:], 16)}\n"



    def Math(self) -> str:
        self.special = self.instructions[self.opcode][SPECIAL]

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
                expected="Expected 3 arguments (&, &, &)."
            )

        return f"{self.bin_opcode}_{tobin(self.arg3[1:], 5)}_{tobin(self.arg1[1:], 5)}_{tobin(self.arg2[1:], 5)}_{empty(5)}_{self.special}\n"

    def convert(self) -> str:
        return self.bin_line




        

