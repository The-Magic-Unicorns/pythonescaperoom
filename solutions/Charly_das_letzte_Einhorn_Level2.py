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
            iChr = ord(uChr)
            eChr = chr((iChr + key) %128)
            encrypted += eChr
        return encrypted
    return decrypt(text, 2)
