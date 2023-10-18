'''
    작성일 : 2023년 10월 18일
    작성자 : 202395032 최민호
    설명 : 도시 인구수 구하는 문제
'''
# 리스트 생성
population = ['seoul', 9765, 'busan', 3441, 'incheon', 2954]

# 서울 인구 수 출력
print('서울 인구수 : ', population[1])
# 인천 인구 수 출력 -1 사용
print('인천 인구수 : ', population[-1])

# 처음부터 끝까지 리스트 중에서 2씩 증가하면서
city = population[0::2]
print('도시 리스트 : ', city)

# 이들의 합 출력 total 사용
# 마지막까지 시작을 비우면 처음부터
total = population[1::2]
print('인구의 합 ; ', sum(total))