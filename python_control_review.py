# Python 제어문 복습
# 작성일: 2025-09-15

'''
1. 조건문(if)
- if, elif, else를 사용하여 조건에 따라 다른 코드 실행
- 들여쓰기(indent)로 코드 블록을 구분
'''

# 기본 if문
age = 20
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# elif 사용 예제
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# 중첩 if문
has_id = True
age = 20
if age >= 18:
    if has_id:
        print("입장 가능")
    else:
        print("신분증을 지참하세요")
else:
    print("미성년자 출입금지")

'''
2. 반복문(for)
- 시퀀스(리스트, 튜플, 문자열 등)를 순회
- range() 함수와 함께 자주 사용
- 중첩 반복문 가능
'''

# 기본 for문
for i in range(5):
    print(i)  # 0부터 4까지 출력

# 리스트 순회
fruits = ["사과", "바나나", "딸기"]
for fruit in fruits:
    print(fruit)

# 중첩 for문 (구구단)
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print()  # 단 구분을 위한 빈 줄

# enumerate 사용
for index, value in enumerate(fruits):
    print(f"{index}번째 과일: {value}")

'''
3. while 반복문
- 조건이 참인 동안 반복 실행
- break, continue 문과 함께 사용 가능
'''

# 기본 while문
count = 0
while count < 5:
    print(count)
    count += 1

# break 사용 예제
while True:
    answer = input("계속하시겠습니까? (y/n): ")
    if answer.lower() == 'n':
        break

# continue 사용 예제
for num in range(1, 11):
    if num % 2 == 0:  # 짝수면 건너뛰기
        continue
    print(num)  # 홀수만 출력

'''
4. 반복문 제어
- break: 반복문을 즉시 종료
- continue: 현재 반복을 건너뛰고 다음 반복으로
- else: 반복문이 정상적으로 완료됐을 때 실행
'''

# break와 else 사용 예제
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("반복문 정상 완료")  # break로 인해 실행되지 않음

# continue 활용
numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        continue
    print(f"양수: {num}")

'''
5. 컴프리헨션(Comprehension)
- 리스트, 딕셔너리, 집합을 간단히 생성하는 방법
'''

# 리스트 컴프리헨션
squares = [x**2 for x in range(10)]  # 0~9의 제곱수 리스트

# 조건부 리스트 컴프리헨션
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # 짝수의 제곱만

# 딕셔너리 컴프리헨션
square_dict = {x: x**2 for x in range(5)}

# 집합 컴프리헨션
even_set = {x for x in range(10) if x % 2 == 0}