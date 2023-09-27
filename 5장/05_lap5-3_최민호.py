'''
작성일 : 2023년 9월 27일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 터틀 그래픽으로 여러 개의 원을 그려보자
'''
import turtle as t

t.shape("turtle")

# 펜 이동 - 펜 자국이 남지 않도록 들어서 이동
t.penup
t.goto(-50, -50)
t.pendown() # 이동을 마치면 펜을 내려놓는다.

for i in range(5) :
    
    # 원하는 도형을 입력 받는다. => 변수에 저장.
    num = int(t.textinput("도형그리기", "몇각형의 도형을 그릴까요?"))

    # 도형 그리기
    for i in range(num) :
        t.forward(100)  # 길이 100 (앞으로)
        t.left(360/num)
    
t.done
