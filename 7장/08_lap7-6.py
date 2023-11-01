'''
    작성일 : 2023년 11월 01일
    작성자 : 202395032 최민호
    설명 : Lap 7-6 도시의 이름가 인구를 튜플로 묶어보자.
'''

# 다음과 같은 리스트가 생성된다.
city_info = [('서울', 9796), ('부산', 3441),('인천', 2954),('광주', 1501),('대전', 1531),]

# 최대 인구수 0 ~ 999999999
max_pop = 0
# 최소 인구수 999999999999 ~ 0
min_pop = 999999999999999
total_pop = 0

max_city = None
min_city = None

for city in city_info:
    total_pop += city[1]
    if city[1] > max_pop:
        max_pop = city[1]
        max_city = city
    if city[1] < min_pop :
        min_pop = city[1]
        min_city = city

print('최대 인구 : {0}, 인구 : {1} 천명'.format(max_city[0], max_city[1]))
print('최소 인구 : {0}, 인구 : {1} 천명'.format(min_city[0], min_city[1]))
print('리스트 도시 평균 인구 : {0} 천명'.format(total_pop / len(city_info)))