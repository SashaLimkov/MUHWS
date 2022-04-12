def ex_1():
    a = int(input("Введите число: "))
    if a > 12 or a < 1:
        print("Ошибка")
    elif 3 <= a <= 5:
        print("Весна")
    elif 5 < a < 9:
        print("Лето")
    elif 8 < a < 12:
        print("Осень")
    else:
        print("Зима")


def ex_2():
    side_b = float(input("Длина: "))
    side_a = float(input("Ширина: "))
    if side_a > 0 and side_b > 0:
        S = side_a * side_b
        P = (side_a + side_b) * 2
        print(f"Площадь прямоугольника: {S}")
        print(f"Периметр прямоугольника: {P}")
    else:
        print("Длина не может быть < 1")


def ex_3():
    a = int(input("Введите число "))
    number = a % 10
    if 4 < a % 100 < 21:
        print(f"{a} компьтеров")
    elif number == 1:
        print(f"{a} Компьютер")
    elif 1 < number < 5:
        print(f"{a} Компьютера")
    else:
        print(f"{a} Компьютеров")


if __name__ == "__main__":
    ex_3()
