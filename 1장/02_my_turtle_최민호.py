'''
작성일 : 2023년 9월 13일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : turtle 그리기
'''
import turtle as t # 터틀 모듈을 사용하기 위한 준비
                   # turtle 클래스 객체를 t로 생성. (별명)
                   
t.shape('turtle')  
t.speed(2)      
# 선그리기
#t.forward(200)  # 200px 이동.

# 삼각형 그리기
#t.forward(200)   # 200px 만큼이동
#t.left(120)       # 왼쪽으로 120도 회전.
#t.forward(200)   # 200px 만큼이동
#t.left(120)       # 왼쪽으로 120도 회전.
#t.forward(200)   # 200px 만큼이동

for i in range(5) :
    t.forward(100)
    t.left(144)

t.mainloop()    # 그림판이 사라지지 않는다.
