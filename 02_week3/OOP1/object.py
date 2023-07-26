# 클래스 정의
class Person:
    # 속성(변수)
    blood_color = 'red'      # 클래스로 생성된 모든 인스턴스들이 공유하는 변수(클래스 변수)
                             # 클래스 변수

    # 메서드
    def __init__(self, name):           # __ => 매직 메서드 : 개발자가 직접 호출하지 않음!
        self.name = name # 인스턴스 변수        # 어딘가에서 알아서 동작함 init = 초기화
                                        # 생성자 메서드라고 함
                                        # 인스턴스를 만들 때 자동으로 호출됨
                                        # self(자기자신)인 이유 
                                        # name이라는 위치인자를 생성해둠 -> 값 넣어줘야 함
    
    def singing(self):              # 인스턴스 메서드(인스턴스가 사용하기 때문에)- 각각의 인스턴스에서 호출할 수 있는 메서드
                                    # 인스턴스 변수에 접근하고 수정하는 작업을 진행
        return f'{self.name}가 노래합니다.'


# 인스턴스 생성
singer1 = Person('iu')
singer2 = Person('BTS')


# 메서드 호출
print(singer1.singing())
print(singer2.singing())

# 속성(변수) 사용
print(singer1.blood_color)
print(singer2.blood_color)