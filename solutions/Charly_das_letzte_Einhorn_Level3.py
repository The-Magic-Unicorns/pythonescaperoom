
def run(riddle):
    result = ""
    for word in riddle.split():
        if word.isdigit():
            continue
        result += word[0].lower()
    return result
