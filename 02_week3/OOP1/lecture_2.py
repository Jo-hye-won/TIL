class Library:
    number_of_book = 0   
    def __init__(self, title, author, volumes=1):
        self.title = title
        self.author = author
        self.volumes = volumes
        Library.increase_book(volumes)
    
    # @classmethod 데코레이터 아래에 정의된 메서드는
    
    
    
    
    # 첫번쨰 인재도, 호출한 대상의 소속 class를 첫번째 인자로 넘기도록 바꿈

    @ classmethod
    def increase_book(cls,volumes):
        cls.number_of_book += volumes
    def __str__(self):
        return self.title


book1 = Library('홍길동전','허균')
print(book1)
print(book1.title, book1.author)
print(book1.volumes)

book2 = Library('레미제','빅토',10)
print(book2)
print(book2.title, book2.author)
print(book2.volumes)

# User 클래스에서는
    # 유저 정보 관리 | 유저 정보 : 이름, 나이
class User:
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.increase_user()

    @classmethod
    def increase_user(cls):
        cls.number_of_people += 1
    
    def __str__(self):
        return self.name

    # rental_system 메서드
        # 1. 인자는 유저와 책 인스턴스를 받는다.
        # 2. 대여하고자 하는 책 수도 함께 받는다.
        # 3. 대여하고자 하는 책 수만큼 라이브러리의 총 책수 감소
        # 4. 대여되는 책의 보유 수량 감소
        # 5. 유저 이름과 책이름, 대여 권수 출력
    # rental_system은 무슨 메서드로 만드는게 적합할까?

    @ classmethod
    def rental_system(cls, user,book, volumes=1):


Library.rental_system(person1,book1)





# 등록해야할 유저의 수 = N

N = 4
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]

person1 = User('김준호', 12)

user_list = []
for index in range(N):
    person = User(name[index],age[index])
    user_list.append(person)
print(user_list)



print("=="*20)

# library 클래스에서는
    # 책의 관리 | 책의 정보: 제목, 작성자, 보유 권수 인스턴스 생성
    # 총 보유 책 권수
    # 대여 시스템 메서드

class Library:
    # class 변수 같은 경우에는 반드시 class로 직접 조작하는것이 맞다.
    number_of_book = 0

    def __init__(self, title, author, volumes=1):
        self.title = title
        self.author = author
        self.volumes = volumes
        Library.increase_book(volumes)

    # 함수 위에 @ 형식으로 데코레이터를 정의하게 되면,,,,
    # 그 데코레이터는 (자기에게 맡겨진 기능을 수행) -> 함수
    # @classmethod 데코레이터 아래에 정의된 메서드는
    '''
    def classmethod(func):
        def wrapper():
            # 첫번째 인자로, 호출한 대상의 소속 class를 첫번째 인자로 넘기도록 바꿈
            func(self.class)
    '''
    @classmethod
    def increase_book(cls, volumes):
        cls.number_of_book += volumes

    def __str__(self):
        return self.title
    
    # rental_system 메서드

        # 1. 인자는 유저와 책 인스턴스를 받는다.
        # 2. 대여하고자 하는 책 수도 함께 받는다.
    @classmethod
    def rental_system(cls, user, book, volumes=1):
        # 3. 대여하고자 하는 책 수만큼 라이브러의 총 책수 감소'
        cls.number_of_book -= volumes

        # 4. 대여되는 책의 보유 수량 감소
        # book.volumes -= volumes
        book_volumes = book.decrease_volumes(volumes)
        # 5. 유저 이름과 책이름, 대여 권수 출력
        print(f'{user.name}님이 {book.title}책을 {volumes}만큼 대여하셨습니다.')
        print(f'{book.title}은 {book_volumes}권 만큼 남았습니다.')

    def decrease_volumes(self, volumes):
        self.volumes -= volumes
        return self.volumes

book1 = Library('홍길동전', '허균')
book2 = Library('레미제라블', '빅토르위고', 10)

# User 클래스에서는
    # 유저 정보 관리 | 유저 정보 : 이름, 나이

@staticmethod
def information():
    print('''
    도서관리 서비스입니다.
    책을 등록할 수 있습니다.
    등록되어있는 유저와 책 정보로 책을 대여할 수 있습니다.    
    ''')

Library.information()

class User:
    # 클래스 변수
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.increase_user()

    @classmethod
    def increase_user(cls):
        cls.number_of_people += 1

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

# N = 등록해야할 유저의 수 
N = 4
name = ['김시습', '허균', '남영로', '빅토르위고']
age = [10, 20, 30, 40]

person1 = User('김준호', 12)
# print(person1)

user_list = []
for index in range(N): # 0 1 2 3
    # persone = User('김시습', 10)  | index : 0
    # persone = User('허균', 20)    | index : 1
    person = User(name[index], age[index])
    user_list.append(person)

# print(user_list)
# for index in range(N): # 0 1 2 3
#     # persone = User('김시습', 10)  | index : 0
#     # persone = User('허균', 20)    | index : 1
#     person = list([name[index], age[index]])
#     user_list.append(person)
# print(user_list)

Library.rental_system(person1, book1)