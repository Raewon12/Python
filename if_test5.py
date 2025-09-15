# 논리 연산자를 사용
# 나이가 18이상(성인)이면서 주민번호를 가진 사람은 "입장 불가"
# age = input()

has_id= True
age = int(input("나이를 입력하세요 :  "))



if(age>=18 and has_id):
  print("입장가능")
elif(age<18 and has_id):
  print("입장불가")
else:
    print("입장불가")   
print("종료")
      
      
      
      
      
      
      
      
    