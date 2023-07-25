# Q4. 혈액형 타입을 담은 blood_types리스트가 주어 질 때,
# 각 혈액형 타입을 키로, 누적 수를 valur로 하는 딕셔너리 blood를 만들어 반환하는
# 함수 make_blood를 작성하시오.


# make_blood(blood_types) -> {'A': 3, 'B': 3, 'AB': 2, 'O': 2}

def make_blood(blood_types):
    # 최종 결괏값
    blood = dict()
    # 주어진 리스트를 순회하면서
    # 각 타입별 등장 횟수를 세어야 한다.
    # 타입별로 최종 결과값 만들어서 저장
    A = 0
    B = 0
    AB = 0
    O = 0
    for item in blood_types:
        if item == 'A':
            A += 1
        elif item == 'B':
            B += 1


    return blood

blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'AB', 'A', 'B']

