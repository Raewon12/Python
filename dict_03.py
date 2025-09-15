# 딕셔너리 생성
# 딕셔너리에서 값을 추가
# 딕셔너리 삭제
# 딕셔너리 특정 키의 데이터를 수정

student={"name":"홍길동","age":20,"score":95}
student["height"]=180
print(student)
del(student["name"])
print(student)
student["age"]=30
print(student)
print(student["age"])
print(student["score"])

# 순환문과 연결
for i in student:
    print(f'key={i} value={student[i]}')