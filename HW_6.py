def ex_1():
    numbers_list = input("Введите числа через пробел ").split()
    print("-".join(numbers_list))


ex_2 = lambda x, y: (x * y) // 2
# def ex_2(x, y): return (x * y) // 2




def ex_3():
    string_list = input("Введите данные через пробел ").split()
    num_list = [
        int(i) for i in input("Введите числа через пробел ").split() if i.isdigit()
    ]
    zipped = zip(num_list, string_list)
    return list(zipped)


if __name__ == "__main__":
    # pass
    # # ex_1()
    # print(ex_2(2,3))
    print(ex_3())
