# Python 함수 복습
# 작성일: 2025-09-15

'''
1. 함수 기본
- def 키워드로 함수 정의
- 매개변수(parameter)와 인자(argument)
- return으로 값 반환
'''

# 기본 함수 정의
def greet(name):
    """
    사용자 이름을 받아 인사말을 출력하는 함수
    """
    return f"안녕하세요, {name}님!"

# 함수 호출
print(greet("홍길동"))

'''
2. 매개변수 유형
- 필수 매개변수
- 기본값 매개변수
- 가변 매개변수(*args)
- 키워드 가변 매개변수(**kwargs)
'''

# 기본값 매개변수
def power(base, exponent=2):
    return base ** exponent

print(power(2))      # 4 (기본값 사용)
print(power(2, 3))   # 8 (기본값 대신 3 사용)

# 가변 매개변수
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15

# 키워드 가변 매개변수
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="홍길동", age=20, city="서울")

'''
3. 반환값
- return 문으로 값 반환
- 여러 값 반환 가능 (튜플로 반환)
- return 없으면 None 반환
'''

# 여러 값 반환
def get_coordinates():
    x = 10
    y = 20
    return x, y  # 튜플로 반환

x, y = get_coordinates()
print(f"x: {x}, y: {y}")

'''
4. 람다 함수
- 익명 함수
- 한 줄로 간단한 함수 정의
- lambda 매개변수: 표현식
'''

# 일반 함수와 람다 함수 비교
def multiply(x, y):
    return x * y

# 같은 기능의 람다 함수
multiply_lambda = lambda x, y: x * y

print(multiply(3, 4))        # 12
print(multiply_lambda(3, 4)) # 12

# 람다 함수 활용 예제
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

'''
5. 함수형 프로그래밍 도구
- map(): 시퀀스의 각 요소에 함수 적용
- filter(): 조건을 만족하는 요소만 선택
- reduce(): 시퀀스를 하나의 값으로 줄임
'''

from functools import reduce

# map 예제
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# filter 예제
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# reduce 예제
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120 (1*2*3*4*5)

'''
6. 스코프(Scope)
- 지역 스코프(Local): 함수 내부
- 전역 스코프(Global): 모듈 수준
- global 키워드: 전역 변수 수정
'''

# 전역 변수와 지역 변수
global_var = 10

def change_global():
    global global_var
    global_var = 20

def local_var_example():
    local_var = 30
    print(f"지역 변수: {local_var}")

change_global()
print(f"전역 변수: {global_var}")  # 20
local_var_example()