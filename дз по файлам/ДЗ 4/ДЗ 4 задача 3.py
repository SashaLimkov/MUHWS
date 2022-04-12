def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


summa = 0
for i in range(10, 251):
    if is_prime(i):
        summa += i
print(summa)


