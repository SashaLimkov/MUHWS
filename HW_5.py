def ex_1(year: int):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Год Високосны")
        return True
    else:
        print("Год не високосный")


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


def ex_3(string: str):
    file = open("file_name.txt", "r+", encoding="UTF-8")
    text = file.read()
    file.write(string)
    file.close()
    return text


def ex_3_extended(string: str):
    with open("file_name.txt", "w+", encoding="UTF-8") as file:
        text = file.read()
        file.write(string)
    return text


if __name__ == "__main__":
    # pass
    # print(ex_1(1200))
    # print(ex_2([1, 2, 4, 3, -10, 145]))
    # print(ex_3("\nСаша"))
    # print(ex_3_extended("Sasha"))
    if ex_1(2000):
        print("вы родились в високосный год")
    else:
        print("вы родились в обычный год")
