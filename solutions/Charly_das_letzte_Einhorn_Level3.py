import string
def run(riddle):
    result = ""
    for uChr in riddle:
        iChr = ord(uChr)
        if 65 <= iChr <= 90:
            iChr += 32
            uChr = chr(iChr)
        result += uChr
    print(result)
    return result