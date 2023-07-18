# 원주율
# 상수(constant)는 모두 대문자로 작성하기로 암묵적 약속
PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
radius = 15

PI_is = '원주율 : '
radius_is = '반지름 : '
circum = '원의 둘레 : '
area = '원의 넓이 : '

print(PI_is, PI)
print(radius_is, radius)
print(circum, radius * 2 * PI)
print(area, radius * radius * PI)
