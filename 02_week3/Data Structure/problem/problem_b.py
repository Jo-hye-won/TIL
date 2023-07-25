# Q2. 다음은 학생들의 수학 점수를 나타낸 딕셔너리이다.
# 딕셔너리에 있는 점수 중, 80점 이상인 점수만을 가진 새로운 딕셔너리를 생성하는
# 함수 make_new_dict를 작성하시오.

scores = {
    'Alice': 75,
    'Bob': 92,
    'Charlie': 80,
    'David': 60,
    'Eva': 85
}

# make_new_dict(scores) -> {'Bob': 92, 'Charlie': 80, 'Eva': 85}


def make_new_dict(scores):
    # 최종 결과값이 dict형식

    result = dict()
    # dict도 순회가 가능하다. 
    # # dict가 가지고 있던 모든 키 리스트 반환
    # print(scores.keys())
    # # dict가 가지고 있던 모든 value 리스트 반환
    # print(scores.values())
    # # dict가 가지고 있는 모든 키와 벨류를 튜플로 묶어서 리스트 반환
    # print(scores.items())
    # # 언패킹 개념을 활용 할 수 있다.
    for key, val in scores.items(): # 언패킹 되서 튜플형태로 키랑,벨류 할당됨
        # val 80 이상인 애들만 따로 모으기
        if val >= 80:
            result[key] = val

    return result




# def make_new_dict(diction):
#     new_dict = {}
#     for key,value in diction.items():
#         if value >= 80:
#             new_dict[key] = value
       
#     return new_dict

print(make_new_dict(scores))




# dic ={}
# for i in range(len(scores)):
#     if scores[i] >= 80:
        
#     else:
#         continue
# print(dic(lists_80))
