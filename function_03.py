#다양한 매개변수
  # 기본 매개변수, default parameter

def myAdd(num1,num2=0,num3=0): #기본값이 0일 뿐 필요하면 다른 값으로 덮어쓸수 있다.
    # 기본 매개변수는 맨마지막에
    return num1 + num2+ num3

result = myAdd(10)
print(f'result={result}')

result = myAdd(10,20)
print(f'result={result}')