from parser import parse
from compiler_error import VASMCompilationError
from sys import argv

def main():
    try:
        parse(argv[1])
    
    except VASMCompilationError as err:
        err.print_error()

if __name__ == "__main__":
    main()
