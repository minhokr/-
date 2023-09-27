'''
작성일 : 2023년 9월 27일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 터틀 그래픽으로 여러 개의 원을 그려보자
'''

import turtle as t

#t.circle(100)

for count in range(10):
    t.circle(100)
    t.left(360/10)

t.mainloop()   # 종료