# def plus(n):
#     total=0
#     for i in range(n+1):
#         total += i
#     return total

# print(plus(10))

# def my_len(message):
#     print(f"길이는={len(message)}")

# my_len("가나다라")

# def my_fun(name):
#     print(f"{name}님 안녕하세요")

# my_fun("정래원")
# my_fun("철수")
# my_fun("민정")

def kick(num1,num2):
   
    for i in range(num1,num2+1):
        for j in range(1,10):
            print(f"{i}*{j}={i*j}")

kick(2,9)
