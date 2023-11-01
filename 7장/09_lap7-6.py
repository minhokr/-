'''
    작성일 : 2023년 11월 01일
    작성자 : 202395032 최민호
    설명 : Lap 7-6 도시의 이름가 인구를 튜플로 묶어보자.
'''

# 다음과 같은 리스트가 생성된다.
city_info = [('서울', 9796), ('부산', 3441),('인천', 2954),('광주', 1501),('대전', 1531),]

max_pop = city_info[0][1]   # 첫번쨰 항목을 기준으로 둔다.
min_pop = city_info[0][1]
total_pop = 0

max_city = city_info[0][0]  # 첫번쨰 항목을 기준으로 둔다.
min_city = city_info[0][0]

for city, population in city_info:
    total_pop += population
    if population > max_pop:
        max_pop = population
        max_city = city
    if population < min_pop :
        min_pop = population
        min_city = city

print('최대 인구 : {0}, 인구 : {1} 천명'.format(max_city, max_pop))
print('최소 인구 : {0}, 인구 : {1} 천명'.format(min_city, min_pop))
print('리스트 도시 평균 인구 : {0} 천명'.format(total_pop / len(city_info)))