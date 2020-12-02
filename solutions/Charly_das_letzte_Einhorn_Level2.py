def run(text):
    def decrypt(text, key):
        key = key * -1
        return encrypt(text, key)
    def encrypt(text, key):
        reverseText = text[::-1]
        encrypted = caesar(reverseText, key)
        return encrypted
    def caesar(text, key):
        encrypted = ""
        for uChr in text:
            if uChr == ' ':
                encrypted += uChr
                continue
            iChr = ord(uChr) - 97
            eChr = chr((iChr + key) % 26 + 97)
            encrypted += eChr
        return encrypted
    return decrypt(text, 19)
