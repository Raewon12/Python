
# 사용자 입력 처리 함수
# 이름 get_data()
# 파라메터
    # start : 시작값
    # end : 종료값
    # input_str : 가이드문구
# 사용자 입력은  input()
# return 정수로 변환된 입력값

import game_utils as gu
import random as rd
start, end = 1, 100

computer = rd.randint(start,end)

count = 0
game_history = []
while True:
    count += 1
    human = gu.get_data(start,end)    
    #  승자선택 로직
    if gu.check_winner(human, computer,game_history,count):
        break