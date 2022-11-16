file_path = ("test.txt")
with open(file_path, mode='r', encoding="UTF-8") as f:
    filex = f.readlines()
    for i in range(len(filex)):
        filex[i]=filex[i].lstrip()


with open('test.txt', mode='w', encoding="UTF-8") as f:
    f.writelines(filex)