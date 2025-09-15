#간단한 함수
# 함수내의 로직이 한줄로 표현한 함수들
def my_add(a,b):
    return a+b 


# 람다 함수 - 한줄로 표현한 함수 
# 간단한 함수를 즉석에서 만들떄 유용하다
# 무조건 값을 리턴하는 함수다.
test = lambda a,b: a+b

a,b = 10,20
print(f'{a}+{b} = {my_add(a,b)}') 