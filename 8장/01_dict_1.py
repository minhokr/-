'''
    작성일 : 2023년 11월 01일
    작성자 : 202395032 최민호
    설명 : 8.1 키와 값을 가지는 딕셔너리
    
    튜플 = () 리스트 = [] 딕셔너리 = {}
'''

# 빈 딕셔너리 생성
phone_book1 = {}

# 딕셔너리 값 저장. key, value
phone_book1['최민호'] = '010-0000-0000'

print('phone_book1 : ',phone_book1)     # {'최민호': '010-0000-0000'}

# 딕셔너리 값 저장. 2.{key, value}
phone_book2 = {'홍길동' : '010-1234-1234', '최민호' : '010-0000-0000'}
print('phone_book2 : ',phone_book2)

phone_book3 = {}
phone_book3['최민호'] = '010-0000-0000'
phone_book3['가'] = '010-1000-0000'
phone_book3['나'] = '010-2000-0000'
phone_book3['다'] = '010-3000-0000'
phone_book3['라'] = '010-4000-0000'

print('phone_book3 : ',phone_book3)

print(':: 전화번호 phone_book3 출력 :: ')
# 모든 key 출력
print(phone_book3.keys())
# 모든 value 출력
print(phone_book3.values())
# 모든 key, value 출력
print(phone_book3.items())

print()
print(':: 전화번호 phone_book3 items()출력 :: ')
for name, phone_num in phone_book3.items() :
    print(name, ':' ,phone_num)
    
print()
print(':: 전화번호 phone_book3 [keys]로 접근하여 출력 :: ')     # items랑 같다.
for key in phone_book3.keys() :
    print(key, ':', phone_book3[key])
    
print()

print('딕셔너리 작성 시 : (콜론)을 기준으로 key:value 작성')
person_dict = {'name' : '최민호', 'age' : 19, 'calss' : '1학년'}

print('name : ',person_dict['name'])    # 딕녀서니의 'name' 키로 값을 조회하여 출력
print('age : ',person_dict['age'])      # 딕녀서니의 'age' 키로 값을 조회하여 출력

print()

print(':: 정렬 ::')
# phone_book3 를 정렬
# 딕셔너리를 키를 기준으로 정렬하여 리스트로 반환.
print(sorted(phone_book3))

print(':: 키를 기준으로 전체를 정렬 ::')
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x [0])    # [0]번지 : 이름을 기준으로 정렬
print(sort_phone_book3)

print(':: 값을 기준으로 전체를 정렬 ::')
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x [1])    # [1]번지 : 값을 기준으로 정렬
print(sort_phone_book3)

print()

print(':: 항목 삭제 ::')
del phone_book3['최민호']
print(phone_book3)

print(':: 전화 번호 삭제 ::')
phone_book3.clear()
print(phone_book3)