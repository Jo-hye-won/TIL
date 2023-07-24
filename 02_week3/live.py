# # print(help(list))

# text = 'Hello, world'
# new_text = text.replace('world','python',2)
# print(new_text) 


# # extend와 append의 차이
# numbers = [1,2,3]
# numbers2 = [4,5,6]
# # numbers.append(numbers2)
# # print(numbers)  # [1, 2, 3, [4, 5, 6]]

# numbers.extend(numbers2)
# print(numbers)   # [1, 2, 3, 4, 5, 6]


# numbers = [3,2,1]
# # sort 메서드 
# # print(umbers.sort())  # None -> 복사본을 만들지 않았다. 반환이 없다. 원본을 바꿈
# # sorted 함수
# print(sorted(numbers)) # [1,2.3] -> 반환이 있다. 원본은 바뀌지 않았다. 
# print(numbers)  # [3,2,1]

numbers = [1,2,3]

# 1. 할당
list1 = numbers

# 2. 슬라이싱 
list2 = numbers[:]

# 3.
numbers[0] = 100

print(list1)  # [100,2,3] -> 원본에 따라서 바뀜
print(list2)  # [1,2,3] -> 