#사용자로부터 점수를 입력받아서 abcdef핫접
score=int(input("점수를 입력하세요 : "))
print(f'score = {score}')

if score>=90: # 90보다 큰애들
    print("A학점")
elif score>=80:
    print("B학점")
elif score>=70:
    print("C학점")
elif score>=60:
    print("D학점")
else:
    print("F학점")