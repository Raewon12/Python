# 중첩 for

list_1= [11,12,13]
list_2=[10,20]

list_2th = [list_1,list_2]
for i in range(len( list_2th)):
   for j in range(len(list_2th[i])):
        print(f'list_2th[i][j]={list_2th[i][j]}')
        