def ex_2(numbers: list):
    max_n = max(numbers)
    min_n = min(numbers)
    sum_all = 0
    sum_even = 0
    for number in numbers:
        sum_all += number
        if number % 2 == 0:
            sum_even += number
    return sum_all, sum_even, max_n - min_n
