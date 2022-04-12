def ex_1():
    print(len(input("введите строку из слов разделенных пробелами. ").split()))


def ex_2():
    word = "programmer"
    my_dict = {letter: word.count(letter) for letter in word}
    print(my_dict)


def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def ex_3():
    print(sum(i if is_prime(i) else 0 for i in range(10, 251)))


if __name__ == "__main__":
    # ex_1()
    # ex_2()
    ex_3()

    # print(sum([11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    #            73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    #            179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241]))
