def get_triangle_s(a, h):
    return a * h / 2


def get_rectangle_s(a, b):
    if a > 0 and b > 0:
        try:
            a = float(a)
            b = float(b)
            res = a * b
            return int(res) if res == int(res) else res
        except ValueError:
            return "Функция ожидает целые числа"
    return "Функция ожидает числа больше 0"
