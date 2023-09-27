'''
작성일 : 2023년 9월 27일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : range() 함수 
'''

for i in range(3) :  # i 변수에 0~2 값이 저장 됨.
    print(i, end='. ')   # end". " 로 지정하면 줄바꿈 하지 않습니다.
    print("안녕하세요.")
    print("   최민호입니다.")
    
# range(시작값, 숫자 앞까지, 증가값(감소값))
# C언어 -> for(초기값; 조건식; 증감식)

for i in range(1.6):
    print(i, end=" ")
    
print ()

# 10 ~ 1 까지 출력
for i in range(10, 0, -1) :
    print(i, end=" ")