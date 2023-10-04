'''
작성일 : 2023년 10월 04일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 반복을 제어하는 break, continue
        교제 137pg 
'''
# 단어를 입력받는다.
word = input("단어를 입력하세요. : ")

print(" :: break1 ::")


for i in word : 
# 만약 word 안에 a,e,i,o,u 가 들어있다면
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
# 멈춘다
        break
# a,e,i,o,u 가 나오기 전에 단어만 출력
    else :
        print(i, end="")
        
        
print()
        
print(" :: break2 ::")
for i in word : 
    if i in ["a", 'e', 'i','o','u',"A", 'E', 'I','O','U'] :     # 모음을 만나면 종료
        break   # 반복 중단. 반복을 빠져 나간다.
    else :
        print(i, end="")
        
    
print()
        
print(" :: continue ::")
for i in word : 
    if i in ["a", 'e', 'i','o','u',"A", 'E', 'I','O','U'] : 
        continue   # 반복의 처음으로 돌아간다. 아래 문장을 만날 수 없다.
    
    print(i, end="")    # 결과 prgrmng 출력