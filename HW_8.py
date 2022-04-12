def is_key_in_dict(key, some_dict: dict) -> bool:
    return False if not some_dict.get(key) else True


def sum_of_dict_values(some_dict: dict):
    values = [float(i) for i in some_dict.values()]
    summa = sum(values)
    return int(summa) if int(summa) == summa else summa


def is_null_list(list_of_smt: list) -> bool:
    return True if not len(list_of_smt) else False


if __name__ == "__main__":
    users = {"123": 2323, "sadsad": 0, "sds": "2.9", "sdjs": "sd"}
    print(is_null_list([1, 2, 3]))
