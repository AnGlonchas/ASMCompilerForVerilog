
BIN_PATH = "./vbin/"

def open_file(path: str):
    with open(path, "r") as file: # Reads the file
        return file.read()

def tokenize(program: str):
   lines = program.splitlines() # Split the file into lines
   return [word.split() for word in lines]  # Split the line into words or tokens