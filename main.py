from parser import parse
from CompilerError import VASMCompilationError


def main():
    parse("./test.vasm")


if __name__ == "__main__":
    try:
        main()
    except VASMCompilationError as err:
        err.print_error()
