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
'''

import random

print(':: 가위 바위 보 게임 시작 ::')

num = random.randrange(3) # 랜덤으로 0,1,2 생성

# 가위 바위 보 출력
if num == 0 :
    print('가위')
elif num == 1 :
    print('바위')
else :
    print('보')