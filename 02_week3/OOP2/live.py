# class professor:
#   def __init__(self, name, age, department):
#     self.name = name
#     self.age = age
#     self.department = department

#   def talk(self):   # 중복
#     print(f'반갑습니다. {self.name}입니다.')

# class Student:
#   def __init__(self, name, age, gpa):
#     self.name = name
#     self.age = age
#     self.gpa = gpa
  
#     def talk(self):  # 중복
#         print(f'반갑습니다. {self.name}입니다.')


# class Person:
#   def __init__(self, name):
#     self.name = name
  
#   def greeting(self):
#     return f'안녕, {self.name}'


# class Mom(Person):
#     gene = 'XX'

#     def swim(self):
#         return '엄마가 수영'


# class Dad(Person):
#     gene = 'XY'

#     def walk(self):
#         return '아빠가 걷기'


# class FirstChild(Dad, Mom):   # 다중상속 받는 지금 현상태에서 가장 최하위 클래스
#                             # 아빠 클래스부터 상속 받고 있음(상속 순서 중요!)
#   mom_gene = Mom.gene
#   def swim(self):
#     return '첫째가 수영'

#   def cry(self):
#     return '첫째가 응애'

# baby1 = FirstChild('아가')  # 생성자메서드가 없어도 최상위 클래스가 이름을 받고 있으니까 이름을 적어줘야지~!
# print(baby1.cry())  # 첫째가 응애  # 본인의 인스턴스 메서드가 우선순위로 활용됨
# print(baby1.swim())  # 첫째가 수영 # 본인의 인스턴스 메서드가 우선순위로 활용됨
# print(baby1.walk())  # 아빠가 걷기 
# print(baby1.gene)  # XY # 두개가 겹쳤기 때문에 Dad먼저 활용됨
# print(baby1.mom_gene) 

# print(FirstChild.mro()) # [<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>]


# 분할해서!
# try:
#     num = int(input('100으로 나눌 값을 입력하시오: '))
#     print(100 / num)
# except ValueError:
#     print('숫자 입력하라고')
# except ZeroDivisionError:
#     print('왜 0을 입력하는거야??')
# except: 
#     print('에러 발생')


# # 하나로 만들 수 있음
# try:
#     num = int(input('100으로 나눌 값을 입력하시오: '))
#     print(100 / num)
# except (ValueError, ZeroDivisionError):
#     print('제대로 입력해')
    


# try:
#     num = int(input('100으로 나눌 값을 입력하시오: '))
#     print(100 / num)
# except BaseException:
#     print('숫자 입력하라고')
# except ZeroDivisionError:
#     print('왜 0을 입력하는거야??')
# except: 
#     print('에러 발생')

my_list = []

try:
  number = my_list[1]
except IndexError as error:
  print(f'{error}가 발생했습니다.')