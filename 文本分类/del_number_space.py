# -*- coding: UTF-8 -*-
import os

file_path = ("test.txt")
with open(file_path, mode='r', encoding="UTF-8") as f:
    filex = f.readlines()
    #   删去小数点
    for i in range(len(filex)):
        linex = list(filex[i])
        for j in range(min(8,len(linex))):
            if(linex[j]=='.'):
                linex[j]=''
                linex[j-1] = ''
                linex[j+1] = ''
        filex[i] = ''.join(linex)
    #删去左边空格
    # for i in range(len(filex)):
    #     filex[i]=filex[i].lstrip()
    #删去开头数字
    # for i in range(len(filex)):
    #     linex = list(filex[i])
    #   # if((linex[0]>='0' and linex[0]<='9') and (linex[1]>='0' and linex[1]<='9') and (linex[2]<'0' or linex[2]>'9')):
    #     if ((linex[0] >= '0' and linex[0] <= '9') and (linex[1] < '0' or linex[1] > '9')):
    #         linex[0]=''
    #     filex[i] = ''.join(linex)
with open('test.txt', mode='w', encoding="UTF-8") as f:
    f.writelines(filex)