student_tuple = [('11111', '홍길동', '010-1111-1111'), ('22222', '최민호', '010-2222-2222'), ('33333', '이민호', '010-3333-3333')]
student_dict = {}

# 딕셔너리 추가
for id_num, name, phone in student_tuple :
    student_dict[id_num] = [name,phone]
    
for key,value in student_dict.items() :
    print(key, ' : ', value[0])
    
number = input("학번을 입력하시오. : ")
print('{}학생은 {}이며{}입니다.'.format(number,student_dict[number][0],student_dict[number][1]))
