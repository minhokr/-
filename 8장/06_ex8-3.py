'''
    작성일 : 2023년 11월 08일
    작성자 : 202395032 최민호
    설명 : 
    
    1. 3명의 학생 학번, 이름, 전화번호의 3쌍의 요소를 가지는
        student_tuple라는 튜플이 존재한다.
    
    2. 이 튜플을 수정하여 {학번 : [이름, 전화번호]}의 쌍으로
        이루어진 딕셔너리를 만들어 출력하시오.
        (반복문 활용)
         
    3. 이 정보를 이용하여 학생의 학번을 입력받아
        이름과 전화번호를 출력하는 학사정보 프로그램을 작성

    4. student_tuple의 마지막 항목으로 학점을 추가한다.
        이 정보를 바탕으로 딕셔너리를 만들어 출력하시오.
        
    5. 학생의 학점 평균을 출력하시오. 
'''

student_tuple = [('11111', '홍길동', '010-1111-1111'), ('22222', '최민호', '010-2222-2222'), ('33333', '이민호', '010-3333-3333')]

student_dict = {}

# 딕셔너리 추가
for id_num, name, phone in student_tuple :
    student_dict[id_num] = [name,phone]

# 딕셔너리 내용 출력
for key,value in student_dict.items() :
    print(key, ' : ', value)
    
# 학번 입력 받아 이름과 연락처 출력
number = input("학번을 입력하시오. : ")
print('이름 : ', student_dict[number][0])
print('연락처 : ', student_dict[number][1])

# 학점 추가
student_dict['11111'].append(4.3)
student_dict['22222'].append(3.9)
student_dict['33333'].append(4.25)

for key,value in student_dict.items() :
    print(key, ' : ', value)

# 학점 평균 계산
print('전체 학생 평균 학점')
for key,value in student_dict.items() :
    sum = sum + value[2]
    
print(f"평균 : {(sum/len):.2f}")