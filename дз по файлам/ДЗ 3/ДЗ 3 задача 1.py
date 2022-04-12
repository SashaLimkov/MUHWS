import random
import os
import time
import pyfiglet
from progress.bar import IncrementalBar


print(pyfiglet.figlet_format("TAG GAME"))
print("Добро пожаловать в игру пятнашки")
print("Правила: соберите все костяшки в порядке возрастания")
input("Нажмите Enter для начала игры...")

mylist = [10, 22, 35, 44, 60, 69, 78, 100]
bar = IncrementalBar("Загрузка: ", max=len(mylist))
for item in mylist:
    bar.next()
    time.sleep(random.uniform(0, 0.3))
bar.finish()
if os.name == "nt":
    os.system("cls")
else:
    print("Консоль не очищена")
number_list = [i for i in range(1, 16)]
# for i in range(1, 16):
#     number_list.append(i)
number_list.append(" ")
result_list = list(zip(*[iter(number_list)] * 4))
for i in range(len(result_list)):
    result_list[i] = list(result_list[i])
random.shuffle(number_list)
area = list(zip(*[iter(number_list)] * 4))
for i in range(len(area)):
    area[i] = list(area[i])
col_width = max(len(str(num)) for row in area for num in row) + 2
while result_list != area:
    os.system("cls")
    for row in area:
        print("".join(str(num).ljust(col_width) for num in row))
    row1 = int(input("Введите строку, откуда вы хотите переместить элемент: ")) - 1
    column1 = (
        int(input("Введите столбец, откуда вы хотите переместить элемент: ")) - 1
    )
    row2 = int(input("Введите строку, куда вы хотите переместить элемент: ")) - 1
    column2 = (
        int(input("Введите столбец, куда вы хотите переместить элемент: ")) - 1
    )
    if area[row2][column2] == " ":
        if (
            -1 < row1 < 4
            and -1 < row2 < 4
            and -1 < column1 < 4
            and -1 < column2 < 4
        ):
            if row2 == row1 or column2 == column1:
                if abs(row2 - row1) <= 1 and abs(column2 - column1) <= 1:
                    area[row1][column1], area[row2][column2] = (
                        area[row2][column2],
                        area[row1][column1],
                    )
                    continue
    print("Такой ход невозможен")
    time.sleep(1)
    continue
print("Поздравляю, вы победили!")