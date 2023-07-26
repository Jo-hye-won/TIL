# 인스턴스는 본인의 변수가 없으면 클래스의 변수를 찾으러 간다
# 각각의 인스턴스는 독립적이다.

class Person:
    name = 'unknown'

    def talk(self):    # 인스턴스 메서드
        print(self.name)


p1 = Person()
p1.talk()   # unknown

# p2 인스턴스 변수 설정 전/후

p1.address = 'korea'
print(p1.address)   # korea

p2 = Person()
p2.talk()   # unknown

p2.name = 'Kim'
p2.talk()   # Kim

print(Person.name) # unknown
print(p1.name) # unknown
print(p2.name) # Kim
