def get_triangle_s(a, h):
    return a * h / 2


def get_rectangle_s(a, b):
    try:
        a = float(a)
        b = float(b)
        if a > 0 and b > 0:
            res = a * b
            return int(res) if res == int(res) else res
        return "Функция ожидает числа больше 0"
    except ValueError:
        return "Функция ожидает числа"
