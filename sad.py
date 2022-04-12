def sum_pairs(ints, s):
    for num in ints:
        if s-num in ints:
            return [num, s-num]

print(sum_pairs([5, 9, 13, -3], 10))