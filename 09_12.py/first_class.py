# number_input_a=int(input("정수 입력> "))
# print("원의 반지름:", number_input_a)
# print("원의 둘레:", 2*3.14*number_input_a)
# print("원의 넓이:", 3.14 * number_input_a * number_input_a)


#------------------------------------------------------------------



#오류 처리
# num1 = input('숫자를 입력하세요: ')

# num2 = input('숫자를 입력하세요: ')

try:
    num1,num2 = map(int,input('공백을 기준으로 숫자를 입력하세요: ').split())
    calc_lists = [num1+num2,num1-num2,num1*num2,num1/num2]


    print('1. 더하기', end='\t')
    print('2. 뺴기', end='\t')
    print('3. 곱하기', end='\t')
    print('4. 나누기', end='\t')
    choice = int(input('원하는 결과를 입력하세여 '))
    print(f'결과는 = {calc_lists[choice-1]}')
except:
    print('오류 발생')
else:
    print('오류 없음')
    
print('프로그램 종료')