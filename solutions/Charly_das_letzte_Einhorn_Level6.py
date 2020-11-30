def run(riddle):
    import random

    result = []
    all_numbers = set([i for i in range(1, riddle["matrix_size"]**2 + 1)])

    for i in range(riddle["matrix_size"]):
        row = []
        while sum(row) != riddle["magical_sum"]:
            row = random.sample(all_numbers, 3)
            if (1 in all_numbers) and (1 not in row):
                row = []
                continue
        all_numbers = all_numbers.difference(set(row))
        result.append(row)
    return result
