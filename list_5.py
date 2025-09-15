import random # import: 외부모듈(라이브러리) 가져오기   
#랜덤라이브러리중에서 sample함수를 사용하겠다   
random_numbers = random.sample(range(100),5) # 0~99사이의 숫자중에서 5개를 랜덤하게 뽑기
print(random_numbers)

#0~10사이의 랜덤한 정수 1개 뽑기
random_int = random.randint(0,10)

random_numbers =random_numbers = random.sample(range(100),5) # 0~99사이의 숫자중에서 5개를 랜덤하게 뽑기 

random_numbers.append(random_int)

print(50 in random_numbers)
print(random_numbers)

print('-'*50)

#삭제

del random_numbers[0] #그냥삭제
print(random_numbers)

removed_number = random_numbers.pop(0) # pop은 삭제도 하지만 그걸 저장함
print(random_numbers)   
print(removed_number)