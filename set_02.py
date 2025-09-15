#집합연산이 가능하다

import random
list_a = random.sample(range,6)
list_b = random.sample(range(10),4)
find_list =[]
for a in list_a:      
   for b in list_b:
     if  a==b :
      find_list.append(a)

print(f'list_a={list_a}')

print(f'list_a={list_b}')

print(f'find_list={find_list}')
print(f'set(find_list) = {setfind_list}')
   




