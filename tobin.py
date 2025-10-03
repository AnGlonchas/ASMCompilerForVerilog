
def instruct_to_bin(instruction: str):
    match(instruction):
        case "NOP": return "00000000"
        case "ADD": return "00000001"
        case "SUB": return "00000010"
        case "IF": return "00000011"
        case "MORE": return "00000100"
        case "LESS": return "00000101"
        case "ADD": return "00000110"

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