voca="""
게맛살
구멍
글라이더
기차
대롱
더치페이
도리
롱다리
리본
멍게
박쥐
본네트
빨대
살구
양심
이빨
이자
자율
주기
쥐구멍
차량
차박
트라이앵글
""".split()

init_word = '기차'
print('끝말잇기를 하자. 내가 먼저 말할게.\n' + init_word)
spoken_words = [init_word]

# 두음법칙 적용함수
def  trans_first(word):
    s1="냥녀뇨니라락란래량려렷로론뢰료루류륜리"
    s2="양여요이나낙난내양여엿노논뇌요누유윤이"
    tt = str.maketrans(s1,s2)
    return word[0].translate(tt) + word[1:]

while True:
    user_inpput = input('> ')

    if not user_input:
        continue
    elif user_input == "졌다":
        print('야호!')
        break
    elif (
        user_input[0] != spoken_words[-1][-1]
    ):
        print('글자가 안 이어져. 내가 이겼다!')
        break
    elif