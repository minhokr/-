'''
작성일 : 2023년 9월 27일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 반복문 for 사용하기
'''
# 본인 이름 5개 출력하기.
print(":: 내 이름 5개 출력하기. ::")
for i in range(5):
    print(i,"최민호")
    
for i in [1,2,3,4,5]:  # 리스트
    print(i,"최민호")
    
print(":: 리스트로 구구단의 19단 출력하기 ::")
for num in [1,2,3,4,5,6,7,8,9] :
    print(f"19 x {num} = {19*num}")
    
print(":: 문자열 내용 출력. ::")
for i in "Hello" :
    print("i =", i)  # i값 출력


#  도전 문제 5.3
print(":: BTS 멤버 명단 출력 ::")
bts = ["뷔", "제이홉", "알엠", "정국", "진", "지민", "슈가"]

for i in bts :
    print(i)