# # # def calculate_sum(**kwargs):
# # #     print(kwargs)  # {'name': Alice', 'age'=30, 'address'='korea'}

# # # calculate_sum(name='Alice', age=30, address='korea')


# # # Map 함수
# # numbers = [1,2,3]
# # result = map(str, numbers) # str 자리에 내가 정의한 함수를 넣을 수도 있다.

# # print(result)  # <map object at 0x00000281728503D0>
# # print(list(result)) # ['1', '2', '3']



# # result=[] #  빈 리스트를 만들고
# # for number in numbers:
# #     result.append(str(number)) # 인자를집어 넣는다

# # print(result)




# # import sys
# # sys.stdin = open('input.txt')

# # T = int(input())
# # K, N, M = map(int, input().split())


# # # map + lambda
# # numbers = []



# # # Lecture
# # # 함수를 호출하는 행위 -> 평가 후 값을 내는 표현식
# # # def 안에서 print코드를 쓰면 None이 나옴(return할 값이 없음)


# global_var = '글로벌 값'

# def update_value(global_var): # 매개변수
#     print(global_var, '매개 변수로 받은 값')
#     result = global_var * 3  # 글로벌 변수가 가지고 있던 값 활용 가능
#     global_var = '로컬 값'  # 글로벌 변수에 할당된 값에 영향 없이 다른값 재할당 가능

#     return result

# print(update_value(global_var)) # 인자로  global scope변수를 넘김
# print(global_var)


# # map and zip
# def some_func(parm1, parm2):
#     return parm1 + parm2

# print(some_func(1,2))
# print(some_func)

# other_var = some_func
# print(other_var(1,2))

import requests
url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json()
print(response)
