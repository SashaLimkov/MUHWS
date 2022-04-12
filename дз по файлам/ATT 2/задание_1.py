from my_module import get_sum, get_div, get_mult, get_razn

while True:
    user_symbol = input("Введите дейтсвие, которое нужно выполнить +, -, *, / ")
    if user_symbol not in ("+", "-", "*", "/"):
        print("вы ввели не подходящий символ")
        continue
    number_1 = float(input("Введите первое число "))
    number_2 = float(input("Введите второе число "))
    if user_symbol == "*":
        print("Ответ:", get_mult(number_1, number_2))
    elif user_symbol == "/":
        print("Ответ:", get_div(number_1, number_2))
    elif user_symbol == "+":
        print("Ответ:", get_sum(number_1, number_2))
    elif user_symbol == "-":
        print("Ответ:", get_razn(number_1, number_2))
