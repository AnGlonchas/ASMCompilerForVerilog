from CompilerError import VASMCompilationError
from tobin import dec_to_bin, instructions
from os import mkdir, path


def tokenize(program: str):
    lines = program.splitlines()
    return [word.split() for word in lines]


def open_file(path: str):
    with open(path, "r") as file:
        content = file.read()
    return content


def NOP(_: str, line: int, __: list = []):
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


instruction_fns = {
    "NOP": NOP,
    "ADD": Math,
    "SUB": Math
}


def parse(program: str):
    code = open_file(program)
    tokens = tokenize(code)
    i: int = 0

    if not path.exists("./bin/"):
        mkdir("./bin")

    with open("./bin/a.vbin", "w+") as file:
        for line in tokens:
            i += 1
            if line:
                operation = line[0]
                args = line[1:]

                if line[0][0] == "#":  # Comment
                    continue

                if not instruction_fns.get(line[0]):
                    raise VASMCompilationError(
                        name="INVALID_INSTRUCTION",
                        expected=f"Invalid {line[0]} instruction.",
                        line=i
                    )
                    continue

                instruction_fns.get(line[0])(operation, i, *args)
                file.close()
    # print(tokens)
