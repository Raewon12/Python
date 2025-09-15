# 0~100사이의 랜덤한 숫자 10 개를 리스트로 저장

import random
numbers = random.sample(range(100),10)  

#짝수만 출력
print(numbers)

#리스트를 순환한다
#순환하면서 각 데이터가 짝수인지 판단
#짝수이면 미리 준비한 빈 리스트에 추가한다
#모든 순환이 끝나면(for문 끝나면)준비한 리스트를 출력하고 len()이용해서 개수도 확인한다.
a_range=[]
for n in numbers:
 if(n%2==0):
    a_range.append(n)
 
print(f'a_range={a_range}')
print(f'len(a_range)={len(a_range)}')