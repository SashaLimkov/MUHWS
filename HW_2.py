def ex_1():
    a = [1, 2, 3, 4]
    total = 1
    summa = 0
    for elem in a:
        total *= elem
        summa += elem
    print(f"Произведение чисел списка = {total}")
    print(summa)


def ex_2():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 237]
    for elem in a:
        if elem == 237:
            break
        if elem % 2 == 0:
            print(elem)


def ex_3():
    a = [11, 22, 22, 22, 1, 3, 3, 3, 2, 3, 4, 5, 6, 21, 21, 22, 22, 22]
    print(id(a))
    i = 0
    while i < len(a):
        if a[i] % 2 == 0:
            a[i] //= 2
            i += 1
        else:
            a.pop(i)
    print(id(a))
    print(a)


if __name__ == "__main__":
    ex_3()
    # ex_2()
    # ex_1()
