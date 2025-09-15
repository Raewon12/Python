#함수의 정의
#함수의 타입-> 매개변수o 리턴값x
#             매개변수o 
#                       리턴값x
#              매개변수x 리턴값x
#매개변수 종류 기본(뒤에서부터 채운다), 가변(함수내부에서 리스트로 저장)그래서 * 이거 사용, 키워드매개변수-> 딕셔너리 , 가변 키워드

#함수 생성 
 #def 함수명( 옵션 ):
        #내용은 필수고
        #return이 있을 수도 없을 수도
#함수 호출
 #함수 이름 ( 옵션 )
 #함수는 호출이 끝나면 해당 위치에 반환값이 있으면 가지고 온다
 # result = myFunc()
import time

def display_second (count):
    count += 1
    print(f'{count}초')
    time.sleep(1)   # 1초간 지연
    return count

def is_user_continue(count):
     if count % 5 == 0:
       user_input = input('To be Continue(Y/y)').upper()
       if user_input == 'Y':
         return True
       else:
         return False
    
     return True
     

count = 0
is_continue = True
count = 0

while is_continue:
    count = display_second(count) # 1초 간격으로 출력
    is_continue = is_user_continue(count) # 5초 간격으로 진행여부 판단
     # 1초간 지연


#5초단위로 사용자한테 계속 할건지 물어본다.. "To be Continue(Y/y)"
    