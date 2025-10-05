class VASMCompilationError(BaseException):
    def __init__(self, expected: str, line: int, name: str):
        self.expected = expected
        self.line = line
        self.name = name
        super().__init__()

    def print_error(self):
        print("[VASM Compiler]")
        print(f"--> Compilation error ({self.name}):")
        print(f"On line: {self.line} - {self.expected}")
