def get_sred(a, b):
    if a > b:
        return "Чило b не может быть меньше числа a"
    nums = []
    for i in range(a, b + 1):
        if i % 3 == 0:
            nums.append(i)
    return sum(nums) / len(nums)


print(get_sred(1, 10))
