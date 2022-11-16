import random

with open('train1.txt', 'r', encoding='UTF-8') as f:
    filex=f.readlines()
    # random.shuffle(filex)
    flag=0
    listx=[]
    for i in range(len(filex)-1, 0,-1):
        if(flag>=1000):
            break
        listx.append(filex[i])
        flag=flag+1
        filex[i]=''

with open('test_1.txt', mode='w', encoding="UTF-8") as f:
    f.writelines(listx)

with open('train1.txt', mode='w', encoding="UTF-8") as f:
    f.writelines(filex)
