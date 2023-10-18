'''
    작성일 : 2023년 10월 18일
    작성자 : 202395032 최민호
    설명 : 리스트 만들기
'''

# 과일 리스트 만들기
fruits = ['딸기', '바나나', '망고']
print("과일 목록 : " ,fruits)

# 수박 추가 => append() 메소드 사용 (마지막에 추가) 
fruits.append('수박')
print("과일 목록 (수박 추가) : " ,fruits)
fruits.append('포도')
print("과일 목록 (포도 추가) : " ,fruits)

# 포도 추가
fruits = fruits + ['멜론']  # 멜론를 더해서 fruits에 저장   (num = num +1)
print("과일 목록 : (멜론 추가) " ,fruits)

# 리스트에서 + 는 연결이다.
num = [1,2,3] + [4,5,6]    
print("숫자 리스트 : ", num)

# * 연산자 => 리스트를 n번 반복한다.
num = [1,2,3] * 3
print("숫자 리스트 * 3 : ", num)

# in 연산자 => 포함 되는가?
print("과일 목록에 망고가 있나요? : " ,'망고'in fruits)

'''
    index를 활용하여 리스트의 항목에 접근하기 178pg
'''

# 과일 리스트에 있는 과일의 개수?
print('과일 리스트에 있는 과일 개수 : ', len(fruits))
# 과일 리스트 중 제일 첫번쨰 과일은?
print("과일 중 제일 좋아하는 과일은? ", fruits[0])

# 과일 리스트 중 제일 마지막 과일은?
print("과일 중 제일 마지막 과일은? ", fruits[-1])    # -1 = 리스트 마지막 항목에 접근

# 과일 중 가장 큰 과일은?
print("과일 중 가장 큰 과일은? (사전식 순서) ", max(fruits))

# 과일 중 가장 작은 과일은?
print("과일 중 가장 작은 과일은? (사전식 순서) ", min(fruits))

# 정렬
fruits.sort()   # 오름 차순
print('오름차순 정렬 : ', fruits)

fruits.sort(reverse=True)   # 내림차순
print('내림차순 정렬 : ', fruits)

'''
    리스트를 원하는 모양으로 자르는 슬라이싱
'''
print('과일 목록 : ', fruits)
print('과일 리스트 중 2,3,4번 과일은? ',fruits[1:4])    # 1번지 ~ 4번지 앞까지
print('과일 리스트 중 1~3번 과일은? ',fruits[0:3])
print('과일 리스트 중 1~3번 과일은? ',fruits[:3])   # 처음부터 3번지 앞까지
print('과일 리스트 중 3번 과일부터 마지막까지 과일은? ',fruits[2:])     # 2번지 부터 마지막 까지

# 처음부터 끝까지 리스트 중에서 2씩 증가하면서
print('과일 리스트 중 1,3,5번 과일은? ',fruits[::2])

# 처음부터 끝까지 리스트 거꾸로 출력
print('과일을 거꾸로 출력 ',fruits[::-1])

'''
    리스트의 원소 값을 자유롭게 조작해 보자
'''
print()
print("과일 목록 : " ,fruits)

# 원하는 위치에 '두리안' 추가 => insert() 메소드 사용
fruits.insert(3, '두리안')
print("과일 목록 : " ,fruits)

# 위치 찾기 => index() 메소드 사용
print("사과의 위치는? " ,fruits.index('멜론'))

# 멜론을 마지막에 추가
fruits.append('멜론')
print('과일 목록(마지막에 멜론 추가) : ', fruits)

# 멜론의 개수 => count() 메소드 사용
print('멜론의 개수는 ?', fruits.count('멜론'))

'''
    리스트이 항목 삭제
'''
print()

# 멜론 삭제 => remove() 메소드 사용     : 처음만나는 항목 삭제
fruits.remove('멜론')   # 처음 만나는 멜론만 삭제
print('과일 목록(멜론 삭제 후 ) : ', fruits)

# 항목 삭제 => pop() 메소드 사용    : 마지막 항목 삭제
fruits.pop()    # 마지막 항목 삭제
print('과일 목록 (마지막 과일 삭제) : ', fruits)

# del() 키워드 => 포도 삭제
del fruits(0)   # 0번지 항목 삭제
print('과일 목록 (포도(0번지) 삭제) : ', fruits)
