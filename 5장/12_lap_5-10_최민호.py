'''
작성일 : 2023년 10월 04일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 사용자가 입력한 숫자들을 더하는 프로그램 작성.
        사용자가 yes라고 답한 동안에만 숫자를 입력받는다.
'''

# 합계 계산 초기값
total = 0  
asw = "yes"   
# 종료값
while asw == "yes":     
# num에 숫자 저장
    num = int(input("숫자를 입력하세요.(yes or no) : ")) 
# 합계 계산
    total = total + num     
# asw 가 no 라면 사용종료
# asw 가 yes 라면 반복
    asw = input("(yes or no) : ")
# 합계 계산 출력
print("합계 : ", total)