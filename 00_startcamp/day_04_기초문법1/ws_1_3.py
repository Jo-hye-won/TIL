# ws_1_3.py
twinkle = '반짝 반짝'
star = '작은별'
beauty = '아름답게 비치네'
east = '동쪽 하늘'
west = '서쪽 하늘'
to_from = '에서도'

# '동쪽 하늘' + '에서도' = '동쪽 하늘에서도'
east = east + to_from # 표현식
west = west + to_from # 표현식
# '반짝 반짝' '작은별' '아름답게 비치네'
# '동쪽 하늘' '에서도' '서쪽 하늘' '에서도'
# '반짝 반짝' '작은별' '아름답게 비치네'
print(twinkle, star, beauty)
print(east, west)
print(twinkle, star, beauty)