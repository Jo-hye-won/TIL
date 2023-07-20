# # 홀수 /짝수
# num = int(input('숫자를 입력하세요 : '))

# # if statement
# # num 이 홀수라면(2로 나눈 나머지가 1이라면)

# if num % 2 == 1:  # 이게 훨씬 더 명시적!
# # if num % 2:         # 결과가 1이 되기 때문에 이렇게 조건해도 된다.
#     print('홀수입니다.')

# # num 이 홀수가 아니라면(짝수면)
# else:
#     print('짝수입니다.')



# number = int(input('양의 정수를 입력해주세요.: '))
# while number <= 0:
#     if number < 0:
#         print('음수를 입력했습니다.')
#     else:
#         print('0은 양의 정수가 아닙니다.')
    
#     number = int(input('양의 정수를 입력해주세요.: '))  # 다시 while로 넘어감

# print('잘했습니다!')



# # 0-9 요소를 가지는 리스트 만들기
# # 1. 일반적인 방법
# new_list = []
# for i in range(10):
#     if i % 2 == 1:  #  홀수만
#          new_list.append(i)

# print(new_list)

# # 2. list comprehension
# new_list_2 = [i for i in range(10) if i % 2 == 1]
# print(new_list_2)

# new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
# print(new_list_3)


# numbers = ['1', '2', '3' ]
# # 1. for loop 
# new_numbers = []
# for number in numbers:
#     new_numbers.append(int(number))
# print(new_numbers)  # [1, 2, 3]

# # 2. map사용
# new_numbers_2 = list(map(int, numbers))
# print(new_numbers_2)    # [1, 2, 3]

# # 3. list comprehension
# new_numbers_3 = [int(number) for number in numbers]
# print(new_numbers_3)


# enumerate
# result = ['a', 'b', 'c']

# print(enumerate(result)) # <enumerate object at 0x000001E6D63A0F80>
# print(list(enumerate(result))) # 요소 하나하나가 튜플로 되어있음, 인덱스와 함께 있음

# for index, element in enumerate(result):
#     print(index, element, end =" ")




# While 안에 for문 넣기

ye_ls = []
num = 0
while num != 5 :
    for i in range(9):
        if i % 2 == 1:
            ye_ls.append(i)  # [1,2] +[3,4] = [1,2,3,4]로 리스트 합칠수도 있다.
        
    num += 1
print(num)
print(ye_ls)
# print('='* 20)


# ye_ls = []
# num = 0
# while num < 5:
#     for i in range(5):
#         if i % 2 == 1:
#             ye_ls.append(i)
#     num += 1
# print(ye_ls)



# dust=[1,2]
# result =0
# while result < 5:
#     result += 1
#     for i in ragne(2):
#         print(dust[i], 'for')
#     print()
#     print(result, 'while')
#     print('==')



list = [1,2,3,4,5]
while True:
  for i in list:
    if i % 2 == 0:
      print(i)
  break

print('=='* 20)


# num =0
# while num<=5 :
#     print('while')
#     num += 1
#     for i in range(5):
#          print('for')

# print('=='* 20)







# lists = [1,2,3,4,5,6,7,8,9,10]
# for list_ in lists:
#     while list_ > 5 :
#            if list_ % 2 == 0:
#              print(list_)
#             list_ += 1
