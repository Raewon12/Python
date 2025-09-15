#매개변수 o, 반환값 o
#매개변수 o, 반환값 x
#매개변수 x, 반환값 o
#매개변수 x, 반환값 x 

#만들고 사용해보기

def mycoffee(coffee): #매개변수 잇고 반환값 없음
    print(f'난 {coffee}를 좋아한다')

def plus_function(num1,num2): #매개변수 있고 반환값 있고
    result = num1 * num2 
    return result

def eating_lunch(): #매개변수 없고 반환값 있고
    return "탕수육"

def say_hello(): #매개변수 없고 반환값도 없음
    print("안녕~")

mycoffee("바닐라라떼")
print(plus_function(100,9))
print(eating_lunch())
say_hello()