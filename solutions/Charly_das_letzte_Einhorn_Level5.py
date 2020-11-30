def run(riddle):
    def recursive_combinations(input_word, combinations=['']):
        if len(input_word) == 0:
            return combinations
        first_letter = input_word[0]
        reduced_word = input_word[1:]
        combinations = combinations + list(map(lambda x: x + first_letter, combinations))
        return recursive_combinations(reduced_word, combinations)
    return recursive_combinations(riddle).count()
