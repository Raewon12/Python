#함수
#함수명 add 
#파라메터는 두개인데 op1,op2
#반환값은 결과를 반환함

#생성
def add(op1,op2):
    return op1+op2


#사용
numbers = [add(10,20), add(10,20), add(10,20)]
print (numbers)

# 매개변수 받아서 출력하는 함수 함수명은 show_number
# 매개변수명은 data
def show_number(data):
    print(f'numbers={data}')
#사용
show_number(add(10,2))