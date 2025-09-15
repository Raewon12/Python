#raise 예외하기
# try:
#     print("정상코드")
#     print("예외 발생")
#     raise ValueError("테스트")
# except Exception as e:
#     print(f'에러: {e} {e.__class__}  {e.__class__.__name__}') 

#     -----------------------------------------------------------------------------



#사용자 입력 처리 함수
#이름 get_data()
#파라메터
    #start : 시작값
    # end  : 종료값
    # input_str : 가이드 문구 
#사용자 입력은 input()
#return 정수로 변환된 입력값


# def get_num():
#     while True:
#         try:
#             h_num=int(input('정수를 입력하세요(1~100): '))
#             if not 1<= h_num <= 100:
#                 raise ValueError('1~100사이범위 초과')
            
#         except Exception as e:
#             print(f'오류 : {e}')
#         else:
#             print("끝")
#             break
#     return h_num
 
# print(get_num())


# ---------------------------------------------------------------

def get_num():
    num1,num2,num3,num4,num5=  map(int, input("숫자 다섯 개를 입력하세요 (공백으로 구분): ").split())
    K=num1+num2+num3+num4+num5
    J=K/5
    return K,J

total, avg = get_num()
print(f"합계 = {total}, 평균 = {avg}")
