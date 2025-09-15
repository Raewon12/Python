# 가위 바위 보 게임
# 사용자로부터 입력을 받아 컴푸터와 대결하는 간단한 가위 바위 보 게임
# 사용자는 "가위", " 바위", "보" 중 하나를 입력하고, 컴퓨터는 무작위 선택
# 게이므이 승패를 판단하고 결과를 출력합니다
# 가위는 1 바위는 2 보는 3 표현
# 게임이 끝나면 계속할지 물어본다


import random
class RP5Game: 
    choices = {1: "가위",2: "바위",3: "보"}

    def __init__(self):
        self.user_choice=None
        self.computer_choice=None
    
    def get_user_choice(self):
        while True:
            try:
                choice = int (input("가위(1), 바위(2), 보(3) 중 하나를 내세요"))
                if choice in self.choices:
                    self.user_choice = choice
                    break
                else:
                    print("잘못된 입력입니다. 1,2,3,중하나를 입력하세요")
            
            except: