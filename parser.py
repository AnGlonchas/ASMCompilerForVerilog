from compiler_error import VASMCompilationError
from os import mkdir, path
from operations import Math, NOP


def tokenize(program: str):
    lines = program.splitlines()
    return [word.split() for word in lines]


def open_file(path: str):
    with open(path, "r") as file:
        content = file.read()
    return content


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
