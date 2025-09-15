# map 자료 구조의 각 요소에 특정함수를 적용


# str_numbers = ['1','10','100']
# print(str_numbers)
# print(list (map(int,str_numbers)))


# scores = input('국어 영어 수학 점수를 공백을 기준으로 입력하세요 ')
# scores = scores.split()
# print(scores)
# kor,eng,math = map(int,scores)
# print(kor+eng+math)

# list_2 = [10,20,30]
# # 각 요소에 2를 곱해서
# def test(data):
#     return data*2

# print(list(map (test, list_2)))
# list_2 = [10,20,30]
# # 각 요소에 2를 곱해서
# print(list(map)(lambda data:data*2.))



# scores = {"홍길동": 85, "이순신": 92, "강감찬": 78}
# print(scores.items("이순신"))


# 튜플
tuple_1 = (2,3,4,1,3,2,1)
print(tuple_1[0])
# tuple_1[0] = 100
print(tuple_1.count(1))
print(tuple_1.index(1))
