numbers = (i // 3 if i % 5 == 0 else i for i in range(1, 201) if i % 2 == 0)
for number in numbers:
    print(number)
