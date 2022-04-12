def ex_1(year: int):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Год Високосны")
        return True
    else:
        print("Год не високосный")