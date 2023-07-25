# Q1. 1부터 인자로 넘겨받은 숫자까지의 합을 구하는
# 함수 make_sum을 작성하시오.

# make_sum(10) -> 55


def make_sum():
    sip = int(input())
    sums = 0
    for i in range(1,sip+1):
        sums = sums + i
    return sums

result = make_sum()
print(result)


# def make_sum(i):
#     sums = 0
#     for tn in range(1,i+1):
#         sums = sums + tn
#     return sums

# result = make_sum(10)
# print(result)


def make_sum(num):
    # 최종 결과값
    result = 0
    # 1부터 num까지의 수를 다 더한다
    # 순회
    # 반복문
    # for 변수 in 순회가능한 객체:
    for n in range(1,num+1):
        # print(n, result)
        result += n
    return result


