from parser import parse
from compiler_error import VASMCompilationError


def main():
    try:
        parse("./test.vasm")
    except VASMCompilationError as err:
        err.print_error()

if __name__ == "__main__":
    main()
