# import random
# result = print(random.randint(1,5)) #1~5사이의 난수 발생    

# 함수 정의 def 키워드 사용
# def 함수명(Parameter):    
#인자(Argument) : 함수 호출시 전달되는 값
# 반환값(Return Value) : 함수가 호출된 곳으로 돌려주는 값
# return 키워드 사용

# 함수를 사용하는 이유????

def myCalc(x,y):
    '''
    두 개의 값을 받아서 더하는 기능
    x는 숫자
    y는 숫자
    '''
    result = x+y
    return result

def say_hello():
    print("Hello")
#2매개변수가 있고 반환값이 없는 함수

def say_hello_name(name):
    print(f'{name}님 안녕하세요')

import datetime
def get_current_time():
    return datetime.datetime.now()

#---------------------
#만든 함수드 써보기
print(myCalc(1,2))
print(say_hello())
print(say_hello_name('정래원'))
print(get_current_time())