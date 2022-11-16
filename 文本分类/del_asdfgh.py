# -*- coding: UTF-8 -*-
import os

file_path = ("test.txt")
with open(file_path, mode='r', encoding="UTF-8") as f:
    filex = f.readlines()
    for i in range(len(filex)):
        # print(type(line))
        linex = list(filex[i])
        for j in range(len(linex)):
            if (linex[j]=='h' and (linex[j-1]<'a' or linex[j-1]>'z')):
                linex[j]=''
        filex[i]=''.join(linex)
with open('test.txt', mode='w', encoding="UTF-8") as f:
    f.writelines(filex)



