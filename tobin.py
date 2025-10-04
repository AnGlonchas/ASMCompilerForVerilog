

"""

& -> registers
# -> number literal

"""

instructions =  {
    "NOP": "00000000", #No operations
    "ADD": "00000001", #Add two numbers (&, #, #)
    "SUB": "00000010",
    "IF": "00000011",
    "MORE": "00000100",
    "LESS": "00000101",
    "ASSIGN": "00000110",
    "TAG": "00000110",
}

def dec_to_bin(numstr: str):
    num = int(numstr)

    if num == 0:
        return 32*"0"
    elif num == 1:
        return (31*"0")+"1"
    else:
        numbin = ""
        while num > 0:
            module = num % 2
            num = num // 2
            numbin = str(module) + numbin
        #Put the rest of the zeroes
        return (32-len(numbin))*"0" + numbin