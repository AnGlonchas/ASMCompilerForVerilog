def dec_to_bin(numstr: str):
    num = int(numstr)

    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        numbin = ""
        while num > 0:
            module = num % 2
            num = num // 2
            numbin = str(module) + numbin
        return numbin