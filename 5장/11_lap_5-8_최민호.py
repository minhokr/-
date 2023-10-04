'''
작성일 : 2023년 10월 04일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 조건에 따라 반복하는 whlie 문
        교제 131pg
'''

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# i = 0
# while i < 5:
#     t.forward(50)
#     t.right(144)
#     i = i + 1

import turtle as t


for count in range(5):
    t.forward(50)
    t.right(144)

t.mainloop()   # 종료