from tobin import dec_to_bin, instructions
from compiler_error import VASMCompilationError


def NOP(
        _: str,  # Operation name
        __: int,  # line
        ___: list = []  # arguments
) -> str:
    return f"{instructions["NOP"]}_{32*"0"}_{32*"0"}_{32*"0"}\n"


def Math(
        op: str,
        line: int,
        reg: str = "",
        a: str = "",
        b: str = ""
) -> str:
    if (reg[0] != "&"):
        raise VASMCompilationError(
            name="EXPECTED_REG_ERR",
            line=line,
            expected="Se esperaba un registro como argumento de la función"
        )
    if (reg[1:] == ""):
        raise VASMCompilationError(
            name="INVALID_REG_ERR",
            line=line,
            expected="Se esperaba el identificador del registro"
        )

    if (a == "" or b == ""):
        raise VASMCompilationError(
            name="EXPECTED_VALUE_ERR",
            line=line,
            expected="A value was expected."
        )

    return f"{instructions[op]}_{dec_to_bin(reg[1:])}_{dec_to_bin(a)}_{dec_to_bin(b)}\n"
