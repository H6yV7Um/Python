# coding=utf-8

import os

# dir = "C://Users/chenq/PycharmProjects/Python/"
# def digui(path):
#     file_list = os.listdir(path)
#     for file in file_list:
#         if not file.startswith("."):
#             if os.path.isfile(path+file):
#                 if file.endswith(".py"):
#                     print(file)
#                     with open(path+file,"r+",encoding="utf-8") as f:
#
#                         if f.readline().find("coding") == -1:
#                             f.seek(0,0)
#                             text = f.read()
#                             f.seek(0,0)
#                             f.write("# coding=utf-8\n"+text)
#             else:
#                 digui(path+file+"/")
# digui(dir)

with open("C://Users/chenq/Desktop/bd_shop_config.sql", "r", encoding="utf-8") as f1:
    lines = f1.readlines()

with open("C://Users/chenq/Desktop/bd_shop_config.sql", "w", encoding="utf-8") as f2:
    f2.write(lines[0].replace("`", ""))
    for line in lines[1:]:
        # 删除某一行数据可以用not in
        if ("PRIMARY" and " KEY ") not in line:
            if "(" in line:
                index = line.find("(")
                f2.write(line.replace(line[index:-2], "").replace("varchar", "string").replace("`", ""))
            elif " date" in line:
                index = line.find(" date")
                f2.write(line.replace(line[index + 5:-2], "").replace(" date", " string").replace("`", ""))
            elif " timestamp " in line:
                index = line.find(" timestamp")
                f2.write(line.replace(line[index + 10:-2], "").replace(" timestamp", " string").replace("`", ""))
            elif "ENGINE" in line:
                f2.write(line[:1] + "\n")
            else:
                pass
    f2.write("ROW FORMAT DELIMITED\nFIELDS TERMINATED BY '\\001'\nLINES TERMINATED BY '\\n'\nSTORED AS TEXTFILE;")
