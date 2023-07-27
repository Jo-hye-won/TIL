# Classes 상속
## 상속 
> 기존 클래스의 '속성'과 '메서드'를 물려받아 새로운 하위 클래스를 생성하는 것
- 유지보수의 용이성 : 상속을 통해 기존 클래스의 수정이 필요한 겨우, 해당 클래스만 수정하면 되므로 유지보수가 용이해짐


## 메서드 중복 정의(상속 없이 구현하는 경우)
```bash
class professor:
  def __init__(self, name, age, department):
    self.name = name
    self.age = age
    self.department = department

  def talk(self):   # 중복
    print(f'반갑습니다. {self.name}입니다.')

class Student:
  def __init__(self, name, age, gpa):
    self.name = name
    self.age = age
    self.gpa = gpa
  
  def talk(self):   # 중복
    print(f'반갑습니다. {self.name}입니다.')
```

### 상속을 사용한 계층구조 변경
```bash
$class Person:
  def __init__(self, name, age): 
              # 인스턴스 함수는 고민할 필요없이 self 넣고 생각하기!
    self.name = name  # 인스턴스의 인스턴스 변수 name에 첫번째로 들어오는 name을 넣을 것이다. 매개변수 name과 인스턴수 변수(아래의 것)의 name의 이름은 달라도 된다. ★
    self.age = age
    
  def talk(self):   # 메서드 재사용
    print(f'반갑습니다. {self.name}입니다.')  # 인스턴스의 인스턴스변수 name을 가져와야 한다.

class Professor(Person):    # Person을 상속받겠다!
# 상속 하는 방법 : 하위클래스 선언할 때 
# 괄호 안에 부모 클래스의 이름 넣으면 된다.
  def __init__(self, name, age, department):
    self.name = name  # 근데 보면 인스턴스 변수 할당하는 것도 겹친다?
    self.age = age
    self.department = department
  
calss Student(Person)
    def __init__(self, name, age, gpa):
    self.name = name   # 근데 보면 인스턴스 변수 할당하는 것도 겹친다?
    self.age = age
    self.gpa = gpa

p1 = professor('박교수', 49, '컴퓨터공학과')  # 인스턴스 하나
s1 = student('김학생', 20, 3.5)               # 인스턴스 둘

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk() # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk() # 반갑습니다. 김학생입니다.

```


## super()
> 부모 클래스의 메서드를 호출하기 위해 사용되는 내장 함수

```bash
class Person:
  def __init__(self, name, age, number, email):
    self.name = name
    self.age = age
    self.number = number
    self.email = email
    
class Student(Person):
  def __init__(self, name, age, number, email, student_id):
    # 부모클래스의 init 메서드 호출
    # 부모 클래스의 init 함수를 호출할거다. self는 적지 않음!!
    super().__init__(name, age, number, email) 
    # Person.__init__(self, name, age) 이렇게 해도 된다. 
    
    # 하지만, 다중상속에서 문제가 생길 수 있기 때문에 
    # (상속이 많아지고 부모클래스의 이름이 바뀌었을 때 유연하게 대응하기 힘들기 때문에) super라는 내장함수 사용
    # 부모의 상속순서를 생각하지 않고 활용할 수 있다.
    self.student_id = student_id

```

## 다중 상속
> 두 개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정함

```bash
class Person:
  def __init__(self, name):
    self.name = name
  
  def greeting(self):
    return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def __init__(self, name):     # 이렇게 초기 생성메서드 작성해주는게
        super().__init__(name)    # 스타일 가이드에는 맞다!
        self.age = age

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'
     
    def __init__(self, name, age):     # 이렇게 초기 생성메서드 작성해주는게
        super().__init__(name)
        
    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom):   # 다중상속 받는 지금 현상태에서 가장 최하위 클래스
                            # 아빠 클래스부터 상속 받고 있음(상속 순서 중요!)
  mom_gene = Mom.gene # 상속순서는 바꿀 수 없지만 엄마의 유전자를 사용하고 싶으면 이렇게 명시적으로 변수설정 해서 가져가면 된다!!
                    
  def __init__(self, name):     # 이렇게 초기 생성메서드 작성해주는게
      #super().__init__(name)
      Mom.__init__(self, name, age)

  def swim(self):
    return '첫째가 수영'

  def cry(self):
    return '첫째가 응애'



baby1 = FirstChild('아가')  # 생성자메서드가 없어도 최상위 클래스가 이름을 받고 있으니까 이름을 적어줘야지~!
print(baby1.cry())  # 첫째가 응애  # 본인의 인스턴스 메서드가 우선순위로 활용됨
print(baby1.swim())  # 첫째가 수영 # 본인의 인스턴스 메서드가 우선순위로 활용됨
print(baby1.walk())  # 아빠가 걷기 
print(baby1.gene)  # XY # 두개가 겹쳤기 때문에 Dad먼저 활용됨
print(baby1.mom_gene)  # XX  #엄마유전자 사용하고 싶어서 설정해둔거 가져옴

```


### 상속 관련 함수와 메서드
#### mro()
- Method Resulution Order(메서드 해결 순서)
- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
- 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서
  상속관계에 있으면 인스턴스 -> 자식 크래스 -> 부모 클래스로 확장

```bash
print(FirstChild.mro())
# [<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>]

```

## 에러와 예외

### 디버깅
> 버그 : 소프트웨어에서 발생하는 오류 또는 결함 / 프로그램의 예상된 동작과 실제 동작 사이의 불일치
- 디버깅 : 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정 / 프로그램의 오작동 원인을 식별하여 수정하는 작업

### 디버깅 방법
1. prit 함수 활용
- 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection 으로 나눠서 생각
2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
- breakpoint, 변수 조회 등
3. python tutor 활용(단순 파이선 코드인 경우)


## 에러
### 에러 유형
#### 문법 에러 (Syntax Error) 
> 프로그램의 구문이 올바르지 않은 경우 발생(오타, 괄호 및 콜론 누락 등의 문법적 오류)

- 문법 오류 예시
- invalid syntax(문법 오류) 
- assign to literal(잘못된 할당)
- EOL(End of Line) : 문장을 마무리 짓지 않았음
- EOF(End of FIle) : 괄호를 안닫았다.


#### 예외(Exception) 
> 프로그램 실행 중에 감지되는 에러
1. 내장 예외
> 예외 상황을 나타내는 예외 클래스들 : 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용

- ZeroDivisionError : 나누기 또는 모듈롸 연산의 두번째 인자가 0일때 발생
- NameError : 지역 또는 전역 이름을 찾을 수 없을 때 발생
- TypeError : 타입 불일치 / 인자 누락 / 인자 초과 / 인자 타입 불일치
- ValueError : 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고, 상황이 IndexError 처럼 더 구체적인 예외로 설명되지 않는 경우 발생
- IndexError : 시퀀스가 인덱스 범위를 벗어날 때 발생
- KeyError : 딕셔너리에 해당 키가 존재하지 않는 경우 (그런데 .get()을 쓰면 None값을 돌려줘서 error 안낼 수 있음)
- ModuleNotFoundError : 모듈을 찾을 수 없을 때 발생
- ImportError : 임포트 하려는 이름을 찾을 수 없을 때 발생
- KeyboardInterrupt : 사용자가 Control-C 또는 Delete를 누를 때 발생
                    : 무한루프 시 강제 종료
- IndentiationError : 잘못된 들여쓰기와 관련된 문법 오류


## 예외 처리

### try 와 except 
- try 블록 안에는 예외가 발생할 수 있는 코드를 작성
- except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성
- 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는  except 블록으로 이동

- if는 확인하고 진행하지만 트라이는 일단 진행하고 본다.

```bash
try:
  result = 10 / 0
except ZeroDivisionError:
  print('0으로 나눌 수 없습니다.')

```

```bash
try:
  num = int(input('숫자입력 : '))
except ValueError:
  print('숫자가 아닙니다.')

```

> 100을 사용자가 입력한 값으로 나누고 출력하는 코드를 작성해보시오
1. 먼저, 발생 가능한 에러가 무엇인지 예상해보기
```bash
num = int(input('100으로 나눌 값을 입력하시오: '))
print(100 / num)
```
int('a') => 문자열을 int로 형변환 : ValueError
100/int('0') => 0으로 숫자를 나눔 : ZeroDivisionError

2. 발생가능한 에러를 모두 명시하거나 & 별도로 작성하기
```bash
# 분할해서!
try:
    num = int(input('100으로 나눌 값을 입력하시오: '))
    print(100 / num)
except ValueError:
    print('숫자 입력하라고')
except ZeroDivisionError:
    print('왜 0을 입력하는거야??')
except:                    # ex.문법에러
    print('에러 발생') 


# 하나로 만들 수 있음
try:
    num = int(input('100으로 나눌 값을 입력하시오: '))
    print(100 / num)
except (ValueError, ZeroDivisionError):
    print('제대로 입력해')
```

### 내장 예외의 상속 계층구조 주의
- 아래와 같이 예외를 작성하면 코드는 2번째 except 절에 이후로 도달하지 못함
```bash
try:
    num = int(input('100으로 나눌 값을 입력하시오: '))
    print(100 / num)
except BaseException:
    print('숫자 입력하라고')
except ZeroDivisionError:
    print('왜 0을 입력하는거야??')
except: 
    print('에러 발생')

# 하위 클래스부터 해줘야 밑의 except 절에도 도달할 수 있음
# 상위 클래스 먼저 있으면 그 이후의 절에 도달할 수가 없음!
# 제로디비전에러는 베이스익셉션의 하위클래스다.
```

- 내장 예외 클래스는 상속 계층구조를 가지기 때문에 except 절로 분기 시 
반드시 하위 클래스를 먼저 확인 할 수 있도록 작성해야 함
[내장예외클래스 계층구조](https://docs.python.org/ko/3.9/library/exceptions.html)


## EAFP & LBYL
> 예외처리와 값 검사에 대한 2가지 접근 방식

### EAFP
> 예외처리를 중심으로 코드를 작성하는 접근방식 (try-except)
- 허락을 구하는 것보다 용서를 구하는 것이 쉽다.(Easier to Ask for Frogiveness than Permission)
- '일단 실행하고 예외를 처리'
- 코드를 실행하고 예외가 발생하면 예외처리를 수행
- 코드에서 예외가 발생할 수 있는 부분을 미리 예측해서 대비하는 것이 아니라 예외가 발생한 후에 예외 처리
- 예외 상황을 예측하기 어려운 경우에 유용

### LBYL
> 값 검사를 중심으로 코드를 작성하는 접근 방식(if-else)
- 도약하기 전에 확인하는 것(Look Before You Leap)
- '실행하기 전에 조건을 검사'
- 코드 실행 전에 조건문 등을 사용하여 예외 상황을 미리 검사하고, 예외 상황을 피하는 방식
- 코드가 좀 더 예측 가능한 동작을 하지만, 코드가 더 길고 복잡해질 수 있음
- 예외 상황을 미리 방지하고 싶을 때 유용


<비교>
- 일단 키찾으러 가! 없어? 그럼 에러로 가
- 키가 있을까? 키가 있어 그럼 프린트. 키가 없어 그럼 프린트

### as 키워드
> as키워드를 활용하여 에러 메시지를 except 블록에서 사용할 수 있음

```bash
my_list = []

try:
  number = my_list[1]
except IndexError as error:   # 인덱스에러를 변수에 저장해서 사용할 수 있음
                              # 해당 익셉트 구문 안에서만 활용할 수 있다!
                            
  print(f'{error}가 발생했습니다.')

# list index out of range가 발생했습니다.
```