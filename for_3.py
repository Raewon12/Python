#remove
# list_a = [3,2,3]
# for i in range(2):
#  list_a.remove(3)

# print(list_a)

# list_a = [1,2,4,2,3,2 ]
# if 2 in list_a:
#  list_a.remove(2)


# print(f'list_a={list_a}')

# list_a=[1,2,1,2,]
# #list_a.remove(1)
# #print(f'list_a={list_a}')
# #1. solution
# for x in list_a[:]:
#     if x==1:
#         list_a.remove(1)
# print(f'list_a={list_a}')   



# list_a = [1,1,2,3,1,2,3,12,3,21,1,1,1]

# for  i in range(len(list_a)):
    
#     if 1 in list_a:
#         list_a.remove(1)
#     else:
#         break

# print(f'list_a={list_a}')   

numbers=[10,21,32,43,54,65,76,87,98,9,102,329]

for i in numbers:
    if i >=100:
        print("-100 이상의 수: " ,i)