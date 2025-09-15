# list_a = [1,2,"문자열",True,False]
# print(list_a[2][2])
# print(list_a[ : ]) # start_index : end_index-1 #원본을 복사
# print(list_a[ :3]) # 1,2,"문자열"
# print(list_a[3:]) #True, False  
# print(list_a[-2: ]) #True, False
# print(list_a[1:-1]) #2,"문자열",True
# #start index : end_indexx -1 : 1
# print(list_a[: : 2]) # 1,"문자열",False 2개씩 뛰어서 출력   
# print(list_a[ : :-1]) #원본을 역순으로 복사 False,True,문자열,2,1
# print(list_a[3:0:-1]) #True,"문자열",2


list_a=[1,2,3]
list_b=[4,5,6]

print("#리스트")
print(f'list_a {list_a}')
print(f'list_b {list_b}')   
print(list_a+list_b)