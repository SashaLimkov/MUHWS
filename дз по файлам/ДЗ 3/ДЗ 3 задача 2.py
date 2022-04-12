n = int(input("введите количество городов "))
city = []
for i in range(n):
    name = input("Введите название города ").lower()
    if name in city:
        print("No")
        continue
    city.append(name)
print(city)
