# -*- coding: UTF-8 -*-
import os

with open('设备安全.txt', 'r', encoding='UTF-8') as f:
    filex=f.readlines()
    for i in range(len(filex)):
        linex=list(filex[i])
        if(linex[len(linex)-1] == '\n'):
            linex[len(linex) - 1] =''
        linex.append('\t')
        linex.append('5')
        linex.append('\n')
        filex[i]=''.join(linex)

with open('test5.txt', mode='w', encoding="UTF-8") as f:
    f.writelines(filex)
