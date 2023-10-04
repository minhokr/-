'''
작성일 : 2023년 10월 04일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 조건에 따라 반복하는 whlie 문
        교제 127pg
'''

# while 조건식 : => : 반드시 사용
#   들여쓰기로 반복하면서 할일 작성.

# 반복문에서 반드시 종료 조건이 있어야 한다.
# while Ture :  무한반복

under_construction = True  # 공사중

# Ture일 동안 계속 반복 (무한반복)
while under_construction :
    response = input("공사가 완료 되었습니까? : ")
    if response == "예" :   # 종료 조건
        under_construction = False  # 공사 완료.
print("루프를 탈출하였습니다. ")