'''
작성일 : 2023년 9월 27일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 점수를 입력받아 학점을 출력하세요.
        90~100 : A 학점
        80~89 : B 학점
        70~79 : C 학점
        60~69 : D 학점
        0~59 : F 학점
'''
# 1. 정수를 입력 받는다.
# 2. 판단하여 출력한다.

sco = int(input("점수를 입력하세요. : "))

#  첫번쨰 성적처리 (논리 연산 오류)
print(":: 첫 번쨰 성적 처리 ::")

if sco >= 90 :
    print("A 학점 입니다.")
elif sco >= 80 :
    print("B 학점 입니다.")
elif sco >= 70 :
    print("C 학점 입니다.")
elif sco >= 60 :
    print("D 학점 입니다.")
else :
    print("F 학점 입니다.")
    
print() # 빈줄 출력
    
# 정확한 범위 지정.
# 두번째 성적처리
print(":: 두 번쨰 성적 처리 ::")

if sco >= 90 and sco <=100:
    print("A 학점 입니다.")
elif sco >= 80 and sco <=89:  # sco >= 80 && soc <= 89 C코드
    print("B 학점 입니다.")
elif sco >= 70 and sco <=79:
    print("C 학점 입니다.")
elif sco >= 60 and sco <=69:
    print("D 학점 입니다.")
elif sco >= 0 and sco <=59:
    print("F 학점 입니다.")
else :
    print("잘못 입력 하였습니다.")

print()
    
# 점수는 무조선 0 ~ 100 사이입니다. - 아니면 잘못된 입력입니다.
print(":: 세 번쨰 성적 처리 ::")

if 0 <= sco <=100 :
    if sco >= 90 :
        print("A 학점 입니다.")
    elif sco >= 80 :
        print("B 학점 입니다.")
    elif sco >= 70 :
        print("C 학점 입니다.")
    elif sco >= 60 :
        print("D 학점 입니다.")
    else :   # A,B,C,D 학점이 아니면
        print("F 학점 입니다.")    
else :   # 0~100 사이의 점수가 아니면
    print("점수를 잘못 입력하였습니다.")