import os.path


def ex_1(number: int):
    if number < 1 or type(number) != int:
        return 0
    if number == 1:
        return 1
    elif number % 2:
        return number + ex_1(number - 1)
    return 0 + ex_1(number - 1)


FILE_NAME = "text.txt"


# with open(FILE_NAME, 'w') as file:
#     pass


def ex_2():
    while True:
        choice = input(
            "1-Вывести журнал.\n2-Изменить журнал\n3-Удалить обучающегося\n ООООООООООООООООООООООООООООООЧ"
            "ЕНЬ ДЛИННАЯ СТРОКА"
        )
        if choice == "1":
            if os.path.isfile(FILE_NAME):
                with open(FILE_NAME, "r") as file:
                    schedule = file.read()
                if schedule:
                    schedule = eval(schedule)
                    for name, mark in schedule.items():
                        print(name)
                        for subject, mark in mark.items():
                            print(subject, mark, sep=" ")
                        print()
                else:
                    print("Файл пустой")
            else:
                print("Файл не существует")
        elif choice == "2":
            if os.path.isfile(FILE_NAME):
                with open(FILE_NAME, "r") as file:
                    schedule = file.read()
                if schedule:
                    schedule = eval(schedule)
                else:
                    schedule = {}
                name = input("ФИО Ученика: ")
                subject = input("Предмет: ")
                mark = input("Оценка: ")
                if name in schedule:
                    schedule[name].update({subject: mark})
                else:
                    schedule[name] = {subject: mark}
                with open(FILE_NAME, "w") as file:
                    file.write(str(schedule))
        elif choice == "3":
            if os.path.isfile(FILE_NAME):
                with open(FILE_NAME, "r") as file:
                    schedule = file.read()
                if schedule:
                    schedule = eval(schedule)
                    name = input("Введите ФИО ")
                    if name in schedule:
                        schedule.pop(name)
                else:
                    schedule = {}
                with open(FILE_NAME, "w") as file:
                    file.write(str(schedule))
        else:
            print("Данного пункта нет")


if __name__ == "__main__":
    print(ex_1(3))
    # ex_2()
