# Q3. 리스트가 인자로 주어질 때, 리스트의 값을 모두 순회하여 
# 홀수인 경우 3배의 값을, 짝수인 경우 제곱의 값으로 변환하여
# 새로운 리스트 result에 담아 반환하는 
# 함수 make_odd_even를 작성하시오.

# make_odd_even([1, 2, 3, 4, 5]) # [3, 4, 9, 16, 15]


def make_odd_even(numbers):
    result = []
    for num in numbers:
        # 홀수인 경우
        #(3 % 2) >>> 1 : True
        if num % 2 :
            result.append(num * 3)
            
        # 짝수인 경우
        else:
            result.append(num ** 2)
    return result

