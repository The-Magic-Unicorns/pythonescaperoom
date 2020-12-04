def run(word):
    result = ""
    vowels = ["a", "e", "i", "o", "u"]
    for c in word:
        c = c.lower()
        if not c in vowels:
            result += c
    return result
