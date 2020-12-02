def run(riddle):
    def recursive_combinations(input_word, combinations=['']):
        if len(input_word) == 0:
            return combinations
        first_letter = input_word[0]
        reduced_word = input_word[1:]
        combinations = combinations + list(map(lambda x: x + first_letter, combinations))
        return recursive_combinations(reduced_word, combinations)
    return recursive_combinations(riddle).count()

#Version 2

def run2(riddle):
    result = []
    def permutations(input_word, permutation=""):
        if len(input_word) == 0:
            result.append(permutation)
        for i in range(len(input_word)):
            new_permutation = permutation + input_word[i]
            rest_of_word = input_word[0:i] + input_word[i+1:]
            permutations(rest_of_word, new_permutation)
    permutations(riddle)
    return result
