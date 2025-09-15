# Python 기본 문법 복습
# 작성일: 2025-09-15

'''
1. 변수(Variables)
- 파이썬의 변수는 값을 저장하는 컨테이너
- 타입 선언이 필요없음 (동적 타이핑)
'''
# 변수 선언과 할당
name = "홍길동"  # 문자열
age = 20        # 정수
height = 175.5  # 실수
is_student = True  # 불리언

'''
2. 자료형(Data Types)
- 숫자형(Numbers): int, float
- 문자열(String): str
- 불리언(Boolean): True, False
- 리스트(List): 순서가 있는 변경 가능한 시퀀스
- 튜플(Tuple): 순서가 있는 변경 불가능한 시퀀스
- 딕셔너리(Dictionary): 키-값 쌍으로 이루어진 자료형
- 집합(Set): 중복을 허용하지 않는 자료형
'''

# 숫자형 예제
int_num = 10
float_num = 3.14

# 문자열 예제
greeting = "안녕하세요"
name = '파이썬'

# 리스트 예제
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", True, 3.14]

# 튜플 예제
coordinates = (10, 20)
# coordinates[0] = 30  # 에러! 튜플은 변경 불가

# 딕셔너리 예제
person = {
    "name": "홍길동",
    "age": 20,
    "city": "서울"
}

# 집합 예제
fruits = {"사과", "바나나", "딸기"}
# 중복 제거: {"사과", "바나나", "딸기"}

'''
3. 연산자(Operators)
- 산술 연산자: +, -, *, /, //, %, **
- 비교 연산자: ==, !=, >, <, >=, <=
- 논리 연산자: and, or, not
- 할당 연산자: =, +=, -=, *=, /=
'''

# 산술 연산자 예제
add = 5 + 3      # 8
sub = 5 - 3      # 2
mul = 5 * 3      # 15
div = 5 / 3      # 1.6666...
floor_div = 5 // 3  # 1
mod = 5 % 3      # 2
power = 2 ** 3   # 8

# 비교 연산자 예제
x = 5
y = 10
print(x < y)    # True
print(x == y)   # False
print(x >= 5)   # True

# 논리 연산자 예제
is_adult = age >= 18
has_id = True
can_enter = is_adult and has_id

'''
4. 문자열 포매팅(String Formatting)
- f-string
- format() 메서드
- % 연산자
'''

# f-string (권장 방식)
name = "홍길동"
age = 20
print(f"이름: {name}, 나이: {age}")

# format() 메서드
print("이름: {}, 나이: {}".format(name, age))

# % 연산자 (오래된 방식)
print("이름: %s, 나이: %d" % (name, age))

'''
5. 형변환(Type Conversion)
- int(): 정수로 변환
- float(): 실수로 변환
- str(): 문자열로 변환
- list(), tuple(), set(): 시퀀스 형변환
'''

# 형변환 예제
num_str = "123"
num = int(num_str)  # 문자열을 정수로
float_num = float(num)  # 정수를 실수로
back_to_str = str(num)  # 숫자를 문자열로

# 컬렉션 타입 변환
list_to_tuple = tuple([1, 2, 3])
tuple_to_list = list((1, 2, 3))
list_to_set = set([1, 2, 2, 3])  # 중복 제거됨