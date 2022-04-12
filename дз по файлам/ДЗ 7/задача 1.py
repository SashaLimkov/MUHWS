def ex_1(number: int):
    if number < 1 or type(number) != int:
        return 0
    if number == 1:
        return 1
    elif number % 2:
        return number + ex_1(number - 1)
    return 0 + ex_1(number - 1)