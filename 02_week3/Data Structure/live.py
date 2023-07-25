# my_set = {1,2,3}
# my_set.remove(2)
# print(my_set) #{1,3}

# my_set.remove(10)  # keyerror


# my_set = {1,2,3}
# my_set.discard(2)
# print(my_set) #{1,3}

# my_set.discard(10)  # error 발생 안함
# print(my_set.discard(10)) # None


# my_set = {1,2,3}
# element = my_set.pop()

# print(element) # 1
# print(my_set) # {2,3}

# person = {'name':'Alice', 'age':25}
# print(person.pop('age'))
# print(person)


# person = {'name':'Alice', 'age':25}

# print(person.setdefault('country','KOREA'))
# # print(person)


# person = {'name':'Alice', 'age':25}
# other_person = {'name':'Jane', 'gender':'Female'}

# person.update(other_person)
# print(person)

# person.update(age=50, country="KOREA")
# print(person)

# person.update(country="KOREA")
# print(person)




# 혈액형 인원수 세기
# 결과 => {'A':3,'B':3, '0':3, 'AB':3}
blood_types =['A','B','A','O','AB','AB','O','A','B','O','B','O','B','AB']


# 1. []으로 풀기
new_dict ={}
# blood_types을 순회하면서
for blood_type in blood_types:
    # 기존에 키가 이미 존재한다면,
    if blood_type in new_dict:
        # 기존에 키의 값을 +1 증가
        new_dict[blood_type] += 1
        
    # 키가 존재하지 않는다면(처음 설정되는 키)
    else:
        new_dict[blood_type] = 1 
         # blood_type에서 빼온 것을 key로 하고 거기에 값을 1로 준다.
print(new_dict)

# 2. .get()으로 풀기
new_dict ={}
# blood_types을 순회하면서
for blood_type in blood_types:
    
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
    # # 기존에 키가 이미 존재한다면,
    # if blood_type in new_dict:
    #     # 기존에 키의 값을 +1 증가
    #     new_dict[blood_type] += 1       
    # # 키가 존재하지 않는다면(처음 설정되는 키)
    # else:
    #     new_dict[blood_type] =1
print(new_dict)


# .setdefault()
new_dict ={}
for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1
print(new_dict)


# a = [1,2,3]

# # 슬라이싱
# b = a[:]
# b[0] = 100
# print(a,b)

# # copy
# c = a.copy()
# c[0] = 100
# print(a,c)


# # 얕은 복사의 한계
# a = [1,2,[1,2]]    # 리스트 안에 리스트(단계가 깊어졌음)
# b = a[:]
# b[2][0] = 999
# print(a,b)  # 위에서는 b만 바꼈었는데 지금은 a도 바뀌어버림!!


# a = [1,2,[1,2]]
# c = a.copy()    # copy를 해도 그렇다.
# c[2][0] = 999
# print(a,c)

# # 세번째 리스트에서 같은 주소를 참고하고 있어서 그렇다(복사 되다가 말았음)

# # 깊은 복사
# import copy  # 모듈 제공해줌
# original_list = [1,2,[1,2]]

# deep_copied_list = copy.deepcopy(original_list)

# deep_copied_list[2][0] = 999
# print(original_list, deep_copied_list)  # 이렇게 하면 원본리스트는 바뀌지 않음



# a=[1,2,3]
# b= list(a)
# print(b)