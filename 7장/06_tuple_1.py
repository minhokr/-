'''
    작성일 : 2023년 11월 01일
    작성자 : 202395032 최민호
    설명 : 한번 생성하면 그 값을 고칠 수 없는 자료형 : 튜플
'''

# 리스트 생성
color_list = ['red', 'green',' blue', 'orange']

# 튜플 생성
color = ('red', 'green',' blue', 'orange')

# 튜플 생성
print(f'color : {color}')

# color에 black 추가하기
# AttributeError: 'tuple' object has no attribute 'append'
# 튜플은 (추가 삭제)가 안된다.
# color.append('black')

# 인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.
print('color 튜플 : ', color)
print('color 투플 중 2,3,4,번은? : ', color[1:4])
print('color 투플 중 1,2,3,번은? : ', color[0:3])
print('color 투플 중 3번~끝은? : ', color[2:])
print('color 투플 중 1,3,5번은? : ', color[::2])
print('color 투플 중 꺼꾸로 출력은? : ', color[::-1])

# 튜플 끼리의 결합 => + 연산자. 반복 => * 연산자.
colors = color + color
print('color 튜플 : ', colors)
print('color 튜플을 10번 반복 : ', color * 10)