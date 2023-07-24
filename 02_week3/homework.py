
# 아래 함수를 수정하시오.
def count_character(text, char):
    # word = "Hello, World!"
    # type(text) == <class str>
    # str.count()
    # count_result = word.count("o")
    return text.count(char)


# 2개의 문자열을 인자로 넘겨줄 수 있는 함수
result = count_character("Hello, World!","o")

print(result) # 2


def for_count_character(text, char):
    result = 0
    # text 문자를 모두 순회
    # 순회하면서 넘겨받는 알파벳 하나하나를 2번째 값 char 과 비교
    
    for c in text: # c | H, e, l, l, o, , ,' ', W, o, r, l, d
        print(c)
        # 비교햇을 때, 동일하면
        if c == char :
            # 숫자 1 증가 -> 어딘가에 수를 담아서
            result = result + 1

    # 최종 반환해야 하는 값 : 세어진 수
    return result

result = count_character("Hello, World!","o")
print(result) # 2

# 패턴 찾기
# result = ~~




# <최소최대>

def find_min_max(nums):
    # my_list = nums.sort() # 원본을 정렬하는 거라서 변수할당할 필요 없음
    nums.sort()
    min = nums[0]
    max = nums[-1]
    # my_tuple = ','.join(min,max)
    return (min, max)

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)


def find_min_max(nums):
    result = (min(nums), max(nums))
    return result

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)


def find_min_max(nums):
    # 규칙 : 함수의 반환값은 반드시 하나의 객체여야 한다.
    # 파이썬이 알아서 하나의 객체로 만들어준다.
    # 하나의 튜플로 묶어서 반환 해 준다.
    # 1, 7 => (1, 7)
    return min(nums), max(nums)

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)

# ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
def for_min_max(numbers):
    # 최종 결과값
    # 나중에 써야 할 결과값을 담을 수 있는 변수 초기화
    # 최종적으로 담길 값과 같은 type의 값으로 초기화
    # 제약 조건
        # numbers를 이루는 요소의 최소, 최댓값이 얼마인지 범위를 잘 파악한다. 
    min_val = numbers[0]
    max_val = numbers[0]
    # numbers 전체 순회하면서 비교
    for num in numbers:
        # 비교 대상이 필요하다.
        if min_val > num :
            min_val = num
        if max_val < num:
            max_val = num

    return min_val, max_va
result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)


# < 메서드 활용한 문자열 뒤집기>

# 아래 함수를 수정하시오.
def reverse_string(word):
    words = list(word)
    words.reverse()
    resolve = ''.join(words)  # 리스트의 요소들을 하나의 문자열로 변환하기
    return resolve

result = reverse_string("Hello, World!")

# for i in result:
#     return i

print(result)


def reverse_string(word):
    # 일단 뒤집힌 문자열 리스트로 만들기
    reversed_list = list(revrsed(text))

    # 최종 결과값
    result = ""
    
    # 리스트를 전부 순회하면서 하나하나 더한다.
    for char in reversed_list:
        result = result + char
        # print(result)
    return result

result = reverse_string("Hello, World!")
# for i in result:
#     return i
print(list(result(reversed("Hello, World!")))


# join 사용하기
def  method_reverse_string(text):
    # '{seperator}'.join(iterable)
    # '-'.join([1,2,3,4,5])
    # >>> '1-2-3-4-5'
    result ''.join(reversed(text))
    return result
result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)


def  non_built_in_function_reverse_string(text):
    # 최종 결과값
    result =''
    # text모두 순회
    for char in text:
        result = charactor + result
        print(result)
    return result

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)



# <중복 요소제거>

# 아래 함수를 수정하시오.
def remove_duplicates(lists):
    new_lst = []
    sett = set(lists)    # set으로 중복 없애고
    lists2 = list(sett)  # 리스트형식으로 변환한 후 
    new_lst.append(lists2)    # new_lst에 담아주기
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(*result)  # 에스터리스크를 사용해서 리스트 안의 요소만 출력하기(언패킹)


# 아래 함수를 수정하시오.
def remove_duplicates(lists):
    # 중복을 제거한 값들만 모아서 새로운 리스트에 추가
    new_lst = []
    # numbers를 모두 순회

    for num in numbers:
        # 추가 할 거다.
        # 누구를? =-> 아직 new_list에 없는 값이면
        if num not in new_lst:
            new_lst.append(num)
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result) 



def remove_duplicates(numbers):
    return list(set(numbers))   # 원하는 답을 못얻을수 있다. 

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result) 




# <3번>
ef sort_tuple(numbers):
    new_tuple = tuple(sorted(numbers))
    return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)


# str의 메서드들은, 반환값이 있다. 
# 왜? str은 immutable한 속성으로 인해,
#  본래의 값을 임의로 수정할 수 없기 때문에, 
#  메서드라고 하더라도 원본 값을 바굴 수 없다. 
#  복사본을 만들어서 원하는 행위를 한뒤, 반환한다.
#   이때, 원본은 그대로 있다. 


# <5번>
'''
- append : 넘겨받은 객체를 그대로 맨 뒤에 추가

- extend : iterable한 객체의 각 요소를 하나하나 쪼개서 맨뒤에 추가
