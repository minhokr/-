'''
작성일 : 2023년 9월 20일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 선택문 if~else
       정수를 입력받아 짝수인지 홀수인지 판단.
       
       짝수 = 2로 나눈 나머지가 0이다. %, ==
       홀수 = 2로 나눈 나머지가 1이다. (0이 아니다.) !=
'''
# 1. 정수를 입력 받는다.
num = int(input("정수를 입력하세요. : "))
# 2. 판단 - 
if num % 2 == 0 :
    print(num,"은 짝수입니다.")
else :
    print("홀수입니다.")