# def calculate_sum(**kwargs):
#     print(kwargs)  # {'name': Alice', 'age'=30, 'address'='korea'}

# calculate_sum(name='Alice', age=30, address='korea')


# Map 함수
numbers = [1,2,3]
result = map(str, numbers) # str 자리에 내가 정의한 함수를 넣을 수도 있다.

print(result)  # <map object at 0x00000281728503D0>
print(list(result)) # ['1', '2', '3']



result=[] #  빈 리스트를 만들고
for number in numbers:
    result.append(str(number)) # 인자를집어 넣는다

print(result)




import sys
sys.stdin = open('input.txt')

T = int(input())
K, N, M = map(int, input().split())


# map + lambda
 numbers = []



 # Lecture
# 함수를 호출하는 행위 -> 평가 후 값을 내는 표현식
def 안에서 print코드를 쓰면 None이 나옴(return할 값이 없음)

