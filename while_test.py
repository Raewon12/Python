#while 반복횟수가 없다
# while 조건 :
# count = 0
# while count < 10:
#     print(f'순환문={count}')
#     count += 1




import time

count = 0
while True:
    count += 1
    print(count)
    time.sleep(1) #1초간 지연 
    
    #5초 단위로 사용자한테 계속할건지 물어본다 .. "To be countinue? (y/n): "
    if count%5==0:
        answer = input("To be countinue? (y/n):")
        if answer.lower()=='n':
            print("종료합니다")
            break
        else:
            print("계속합니다")
            continue
        