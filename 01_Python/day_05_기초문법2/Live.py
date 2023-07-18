# 진법 변경(10진수 -> n진수)

# print(bin(12))
# print(oct(12))
# print(hex(12))

# print(2 / 3)

# 지수(제곱하는 횟수) 표현 10^
print(314e-2) # 3.14
print(314e2) # 31400.0


print('철수야 \'안녕\'')

# f-string

bugs = 'roaches'
counts = 100
area = 'living room'

print(f'Debugging {bugs} {counts} {area}')

# f-string 쓰기 전에는 아래와 같이 했음
print('Debugging {} {} {}'.format(bugs, counts, area))
print('Debugging %s %d %s' % (bugs, counts, area))

# f-string 응용(f-string advanced)
greeting = 'hi'
print(f'{greeting:>10}') # 오른쪽 끝에 
print(f'{greeting:^10}') # 10칸중에 가운데 두겠다
print(f'{3.141592:.4f}') # 소수점 4자리까지 출력하겠다


# 불변과 가변
my_str = 'hello'
my_str[0] = 'z'

list = [1,2,3]
list[0] =100
print(list)

