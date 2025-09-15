# # 가위 바위 보 게임 (컴퓨터 vs 휴먼)

# import random

# options = ['가위','바위','보']

# user = input("가위 바위 보! : ")

# computer = random.choice(options)
# print(f'computer = {computer}')

# def game(user, computer):
#     if user==computer:
#         return"무승부"
#     elif (user=="가위" and computer=="주먹")or (user=="주먹" and computer=="보")or (user=="보"   and computer=="가위"):
#          return"패배" 
#     else:
#          return"컴퓨터 승리" 
    
# print("결과: " ,game(user , computer))

# ------------------------------------------------------------------

# import random
# #1은 가위 2는 바위 3는 보
# #랜덤하게 선택한 컴퓨터의 값
# com_choice = random.randint(1,3)
# #사용자의 값
# user= int( input("입력(1:가위 2:바위 3:보) : "))
# #승패확인
# def game(com_choice,user):
#    if com_choice == user:
#        print("무승부")
#    elif (user==1 and com_choice==2) or (user==2 and com_choice==3) or (user==3 and com_choice==1):
#        print("패배")
#    else:
#        print("승리")

# print("컴퓨터: ",com_choice)
# print("user: ",user)
# game(com_choice,user)

#///////////////////////////////////////////////////////////////////////////

# import random

# judge = lambda c,u : "무승부" if(c==u) else ("승리" if((c-u)%3==1) else "패배")

# c_choice =  random. randint(1,3)
# user = int(input("입력(1:가위=1, 바위=2, 보=3) : "))

# print(f"컴퓨터={c_choice}, 사용자={user}")
# print("결과:", judge(user, c_choice))

#-------------------------------------------------------------------------

import random
def get_com_num(start=1, end=3):
    '''
    랜덤값출력(start ~ end)    
    '''
    return random.randint(start,end)

def get_human_num():
    return int(input("입력(1:가위 2:바위 3:보) :"))

def check_winner(com_choince, human_choice):
    if com_choince == human_choice:
        print('비겼습니다.')
    else:
        if (com_choince == 1 and human_choice ==2) or \
            (com_choince == 2 and human_choice ==3) or \
            (com_choince == 3 and human_choice ==1):
            print("당신이 이겼습니다.")
        else:
            print("당신이 졌습니다.")