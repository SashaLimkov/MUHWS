def multiply_list_el(num_list):
    result = 1
    for num in num_list:
        result *= num
    return result


print(multiply_list_el([1, 2, 3, 4, 5]))
