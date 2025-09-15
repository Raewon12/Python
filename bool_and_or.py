#and 연산자 or 연산자
#and : 두개 모두 참일떄만 참  ~이고 ~이다
#or : 두개 중 하나만 참이어도 참   ~이거나 ~이다    
#ex) 평균이 60이상이고 각 과목별로 점수가 40점 이상이면 합격
#ex)60세 이상이거나 5세 미만이면 입장료 무료

# math=int(input("수학점수: "))
# eng=int(input("영어점수: "))
# science=int(input("과학점수: "))
# avg=(math+eng+science)/3
# if avg>=60 and math>=40 and eng>=40 and science>=40:
#    print("합격")
# else:
#     print("불합격") 

# age=int(input("나이를 입력하세요: "))
# if(age>=60 or age<5):
#     print("무료입장")   
# else:
#     print("입장료를 내세요")

print(f'(10>0 and 10>100){10>0 and 10>100}')  # 1 X 0 = 0
print(f'(10>0 or 10>100){10>0 or 10>100 }')                        # 1 + 0 = 1    