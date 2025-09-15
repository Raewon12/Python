#명령어는 모두 실행하고 조건문은 특정 명령문은 실행 안댐 
#if 조건 : 
#들여쓰기 해줘야함. if의 하위 명령어로 만든다. 이걸 block이라고함


# age=int(input("나이를 입력하세요 :"))
# if age>=19:
#     print("성인입니다")
# else:
#     print("청소년입니다")

# print("if와 상관없는 명령")

# 조건에 맞으면 합격 틀리면 불합격

# score = int(input("점수를 입력하세요 : "))
# if score>=60:
#       print("합격")
# else:
#     print("불합격")

temperature = 25
if temperature > 30:
     print("너무 더워요")
elif temperature > 20:
     print("날씨가 좋아요") 
elif temperature > 10:
     print("조금 쌀쌀해요")
else:
     print("날씨가 추워요")