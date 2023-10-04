'''
작성일 : 2023년 10월 04일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 심화문제 5-2, 141pg
        1. 두 수를 입력받아서 두수의 합계를 출력하기.
        2. 두 수 사이의 짝수의 합계 출력하기 
'''

# 두 정수를 입력 받는다.
num1 = int(input("첫 번쨰 수를 입력하세요. : "))
num2 = int(input("두 번쨰 수를 입력하세요. : "))

# 만약 대와 소가 바뀐다면
if num1 > num2 :
    num1, num2 = num2, num1
    
# 두 수의 합 구하기
i = num1
sum = 0
while i <= num2:
    sum = sum+i
    i += 1
print(" 두 수의 합은 {}입니다.".format(sum))

# 두 수의 짝수 구하기
i = num1
sum = 0
while i <= num2 :
    if i % 2 == 0 :
        sum = sum+i
    i += 1
print("두 수의 짝수의 합은 {}입니다." .format(sum))