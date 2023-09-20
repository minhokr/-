'''
작성일 : 2023년 9월 20일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 선택문 if~else
       random 을 이용한 가위바위보 게임.
       
       random 함수로 생성된 정수를 가지고 게임을 진행합니다.
       0 = 가위
       1 = 바위
       2 = 보
       
       두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다.
'''

import random

print(':: 가위 바위 보 게임 시작 ::')

player1 = input('plater1의 이름 : ')
player2 = input('plater2의 이름 : ')

num1 = random.randrange(3) # 랜덤으로 0,1,2 생성
num2 = random.randrange(3) # 랜덤으로 0,1,2 생성

# 가위 바위 보 출력
print(player1, " : ", end="")
if num1 == 0 :
    print('가위')
elif num1 == 1 :
    print('바위')
else :
    print('보')
    

# 가위 바위 보 출력
print(player2, " : ", end="")
if num2 == 0 :
    print('가위')
elif num2 == 1 :
    print('바위')
else :
    print('보')
    
if num1 == (num2 + 1 ) %3 :
    print('player1의 승리입니다')
elif num1 == num2 :
    print('비겼습니다.')
else :
    print('player2의 승리입니다.')
    

