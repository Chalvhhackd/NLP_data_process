# -*- coding: UTF-8 -*-
import os

file_path = ("test.txt")
with open(file_path, mode='r', encoding="UTF-8") as f:
    #删去过长行
    # filex = f.readlines()
    # for i in range(len(filex)):
    #     linex=list(filex[i])
    #     if(len(linex) >= 100 ):
    #         linex=''
    #     filex[i]=''.join(linex)

    # 合并行
    # filex = f.readlines()
    # for i in range(len(filex)):
    #     linex=list(filex[i])
    #     if(linex[len(linex)-2] !='。' and linex[len(linex)-2] !='；'):
    #         linex[len(linex)-1]=''
    #     filex[i]=''.join(linex)

    # 去重
    # filex=f.readlines()
    # for i in range(len(filex)):
    #     if(i>=1 and filex[i]==filex[i-1]):
    #         filex[i]=''

    # 断句
    # filex = f.readlines()
    # for i in range(len(filex)):
    #     linex=list(filex[i])
    #     for j in range(len(linex)):
    #         if((linex[j]=='。' or linex[j]=='；' or linex[j]=='：' ) and linex[j+1]!='\n'):
    #             str1=linex[j+1:len(linex)]
    #             str2=linex[0:j+1]
    #             str2.append('\n')
    #             linex=str2+str1
    #     filex[i]=''.join(linex)
    # 删去括号
    filex=f.readlines()
    for i in range(len(filex)):
        linex=list(filex[i])
        if(len(linex)>=3):
            if(linex[1]=='）'):
                linex[0]=''
                linex[1]=''
            elif(linex[0]=='）'):
                linex[0]=''
        filex[i]=''.join(linex)
    # 删去空行
    # filex = f.readlines()
    # for i in range(len(filex)):
    #     linex = list(filex[i])
    #     if(linex[0]== ' ' and linex[1]=='\n' and len(linex)<=2 ):
    #     # if(linex[0]==' ' and len(linex)==1):
    #         linex=''
    #     filex[i]=''.join(linex)
with open('test.txt', mode='w', encoding="UTF-8") as f:
    f.writelines(filex)