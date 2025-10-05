from tobin import dec_to_bin, instructions, empty32
from compiler_error import VASMCompilationError

def NOP(
        _: str,  # Operation name
        __: int,  # line
        ___: list = []  # arguments
    ) -> str:

    return f"{instructions["NOP"]}_{empty32}_{empty32}_{empty32}\n"


def Math(
        op: str,
        line: int,
        arg1: str = "",
        arg2: str = "",
        arg3: str = ""
    ) -> str:

    if arg1[0] != "&" or arg2[0] != "&" or arg3[0] != "&":
        raise VASMCompilationError(
            name="EXPECTED_REG_ERR",
            line=line,
            expected="Expected a register as an argument."
        )

    if not (arg1 or arg2 or arg3):
        raise VASMCompilationError(
            name="INVALID_REG_ERR",
            line=line,
            expected="Expected a register identificator."
        )

    return f"{instructions[op]}_{dec_to_bin(arg1[1:])}_{dec_to_bin(arg2[1:])}_{dec_to_bin(arg3[1:])}\n"
