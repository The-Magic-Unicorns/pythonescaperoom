def run(riddle):
    result = ""
    for word in riddle.split():
        if word.isdigit():
            continue
        # This means not all poitions in word are numeric, now it could be iterated over word using different methods:
        # via char index
        # via similar for loop as above
        # via slicing operator
        # this is not necessary in our example but described in our slides
        result += word[0].lower()
    return result
