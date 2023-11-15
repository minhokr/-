'''
    작성일 : 2023년 11월 15일
    작성자 : 202395032 최민호
    설명 : 문자열
'''

text = "There's a reason some people are working to make\
    it harder to vote, especially for people of color.\
        It’s because when we show up, things change."
        
# 띄어쓰기로 분자열을 분리하고, 단어의 개수를 찾아라.
# len() = > 개수(길이) : 리스트의 항목 개수 찾는 함수


#text2 = text.split()
#print(text2)
#print('word count : ', len(text2))


# 도전문제 9-1
# 회사이름은 **로 표시
# KT, Sansung, LG, SKT

text0 = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
        Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
        U+ Mystic Pink 30%, SKT Mystic Blue not disclosed)'

# 모든 문자를 소문자로 변경
# 소문자로 바꾼 단어들을 공백으로 구분한다.
# 구분된 단어를 검사한다.(판단) => 단어가 kt or samaumg or lg or skt 인가?
# 검사하는 단어가 회사명이면 **로 바꾼다.
# 아니면 그 단어는 그대로 출력한다.
# 결과 출력
for word in text0 :
    if word == "kt" or word == 'samsung' or word == 'lg' or word == 'skt':
        text0 += word.replace(word,'**')
    else : 
        text0 += word + ' '
print('text2 : ',''.join(text0))