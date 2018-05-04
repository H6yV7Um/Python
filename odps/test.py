# coding=utf-8
dir = "C://Users/chenq/PycharmProjects/Python/"
for file in dir:
    if file.endswith(".py"):

        with open(file, "r+", encoding="utf-8") as f:
            text = f.read()
            f.seek(0, 0)
            f.write("# coding=utf-8\n" + text)