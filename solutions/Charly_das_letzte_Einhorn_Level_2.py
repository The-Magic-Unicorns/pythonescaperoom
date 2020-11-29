### Solution for "Charly das letzte Einhorn" - level 2
def run(text):
    deCrypted = ""
    key = -2
    for uChr in text:
        iChr = ord(uChr)
        eChr = chr((iChr + key) % 128)
        deCrypted += eChr
    reverseText = deCrypted[::-1]
    return reverseText
