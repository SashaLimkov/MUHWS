def ex_3(string: str):
    file = open("file_name.txt", "r+", encoding="UTF-8")
    text = file.read()
    file.write(string)
    file.close()
    return text

