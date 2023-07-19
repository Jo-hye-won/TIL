# 함수
> 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
- 사용하는 이유 
1. 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
2. '재사용성'이 높아지고, 코드의 '가독성과 유지보수성' 향상
```bash
# 두 수의 합을 구하는 코드
num1 = 5
num2 = 3
sum = num1 + num2
print(sum)

# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
    return num + num2

# 함수 사용하여 결과 출력
num1 = 5
num2 = 3
sum = get_sum(num1, num2)
print(sum)

```
## 내장 함수(Bulit-in function)
> 파이썬이 기본적으로 제공하는 함수(별도의 import 없이 바로 사용 가능)

- 예시 : 절대값을 만드는 함수 abs / print()도 내장 함수

```bash
# abs 함수 호출의 반환 값을 result에 할당
result = abs(-1)
print(result) #1
```
[함수 알수 있는 사이트] (https://docs.python.org/3.9/)
> 자습서랑  Library  reference로 검색하기

### 함수 호출(function call)
> 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것


### 함수 구조
- 들어가는 값 : input = 매개변수(parameter)
- 들여쓰기 이후에 작성된 부분 -> 몸통(function body)
- """ """ => Docstring () = 함수에 대한 설명서 작성 ->body의 상단에 작성
- output: 나오는 값, 반환값(return value)

```bash
def make_sum(pram1, pram2):
    """이것은 두 수를 받아 두 수의 합을 반환하는 함수입니다.

    >>> make_sum(1,2) 
     3 
    """

    return pram1 + pram2

```

### 함수의 정의와 호출
> 함수의 정의
- 함수 정의는 def 키워드로 시작(define의 약자)
- def 키워드 이후 함수 이름 작성
- 괄호 안에 매개변수를 정의할 수 있음
- 매개 변수(parameter)는 함수에 전달되는 값을 나타냄

```bash
# 함수 정의
 def greet(name):
 """입력된 이름 값에 인사를 하는 메세지를 만드는 함수
 """
 message = 'Hello, ' + name
 return message

# 함수 호출
result = greet('Alice')
print(result)

```

#### 함수 body
- 콜론(:) 다음에 들여쓰기 된 코드 블록
- 함수가 실행될 때 수행되는 코드를 정의
- Docstring은 함수 body 앞에 선택적으로 작성 가능한 함수 설명서

#### 함수 반환 값
- 함수는 필요한 경우 결과를 반환 할 수 있음
- return 키워드 이후에 반환할 값을 명시
- return 문은 '함수의 실행을 종료'하고, 결과를 호출 부분으로 반환

> ★★★ print는 어떤 값을 주는 함수는 아니고 그냥 출력해주는 것 
반환이라고 하는건 어떤 변수에 담아서 쓸수 있는 건데 print는 값을 반환(return)해 주는게 아니라 그냥 출력해주는 것!! ★★★
```bash
# 함수 정의
def greet(name):
    message = 'Hello, ' + name
    return message #  이 리턴이 없으면 밑에  result에 할당해줄 값이 없어서 print에서 None이 나오게 됨

result = greet('Alice')
print(result)

```

#### 함수 호출
 - 함수를 호출하기 위해서는 함수의 이름과 필요한 인자(argument)를 전달해야 함
 - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨


 ## 매개변수(parameter)와 인자(argument)
 > 매개변수(parameter) : 함수를 '정의'할 때, 함수가 받을 값을 나타내는 변수 

 > 인자(argument) : 함수를 '호출'할 때, 실제로 전달되는 값
```bash
def add (x, y) : # x, y는 매개변수
    result = x + y
    return result
# ----------------------------------------
a=2
b=3
result = add(a,b): # a와b는 인자

```

# 인자의 종류
## 1. Positional Arguments (위치인자)
> 함수 호출 시 인자의 위치에 따라 전달되는 인자
- ★ 위치인자는 함수 호출 시 반드시 값을 전달해야 함
```bash
            1   2
def greet(name, age): # name은 첫번째 인자, age는 두번째 인자 # 위치인자
    print(f'안녕하세요, {name}님! {age}살이시군요.')
        1       2
greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.
greet(25, 'Alice') # 안녕하세요, 25님! Alice살이시군요.
```

## 2. Default Argument Values (기본 인자 값)
> 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
```bash
def greet(name, age=30):  # age를 30으로 기본값 할당해 둠 # 기본 인자 값설정
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob') # 인자를 하나만 넣어도 출력 됨 # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40) # 이렇게 둘 다 넣게 되면 30이 아니라 40 나온다!
```

## 3. Keyword Arguments (키워드 인자)
> 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
- 단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함
```bash
def greet(name, age):  # 위치 인자로 돌아감
    print(f'안녕하세요, {name}님! {age}살이시군요.')
 
# 키워드 인자로 하면 순서 안지켜도 된다.
greet(name='Alicd', age=25) # 안녕하세요, Alice님! 25살이시군요.
greet(age=25, name= 'Alice') # 안녕하세요, Alice님! 25살이시군요.
greet(age=25, 'Alice') # 위치 인자가 키워드 인자 이후에 따라오고 있다고 함(오류 뜸)  위치 인자 이후에 키워드 인자가 와야 함!!

```

## 4. Arbitary Argument Lists (임의의 인자 목록)
> '정해지지 않은 개수의 인자'를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '*(에스터리스크)'를 붙여 사용하며, 여러 개의 인자를 tuple(파이썬이 내부 동작을 위해서 쓰는 것)로 처리


```bash
def calculate_sum(*args):
    print(args)      # (1, 2, 3) 과 같이 임의의 인자목록을 받고 있음 (튜플로)
    total = sum(args)
    print(f'합계: {total}')

"""
(1, 2, 3)
합계: 6
"""
calculate_sum(1, 2, 3)
```


## 5. Arbitrary Keyword Argument Lists (임의의 키워드 인자 목록)
> 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '**'를 붙여 사용하며, 여러 개의 인자를 dictionary로 묶어 처리
```bash
def calculate_sum(**kwargs):
    print(kwargs)  # {'name': Alice', 'age'=30, 'address'='korea'}

calculate_sum(name='Alice', age=30, address='korea')
```


### 함수 인자 권장 작성순서
> 위치 - 기본 - 가변 - 키워드 - 가변 키워드
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
- 단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있음
        가변인자        기본인자
​print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)


# Python의 범위(Scope)
> 함수는 코드 내부에 local scope(지역 함수)를 생성하며, 그 외의 공간인 global scope(전역함수)로 구분
- scope 
1. global scope : 코드 어디에서든 참조할 수 있는 공간
2. local scope : 함수가 만든 scope(함수 내부에서만 참조 가능)

- variable
1. global variable : global scope에 정의된 변수
2. lacal variable : local scope에 정의된 변수

### Scope 예시
- num은 local scope에 존재하기 때문에 global 에서 사용할 수 없음
- 이는 변수의 수명주기와 연관이 있음
```bash
de func():
    num = 20  # <- 지역에 존재 
    print('local', num) # local 20

func()
print('global', num) # NameError : name 'num' is not defined
                        # num이 local scope에 있지  global scope에 존재하는게 아니기 때문에 존재하지 않음
```

### 변수 수명주기(lifecycle)
> 변수의 수명주기는 변수가 선언되는 위치와 스코프에 따라 결정됨
1. bulit-in scope : 파이썬이 실행된 이후부터 영원히 유지  ex) 내장함수
2. global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지


### 이름 검색 규칙(NAme Resolution)
> 파이썬에서 사용되는 이름(식별자)뜰은 특정한 이름공간에 저장되어 있음
> 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름
 1. Local scope : 지역범위(현재 작업 중인 범위)
 2. Enclosed scope : 지역범위 한 단계 위 범위 : 함수안에 함수 있을 때
 3. Global scope : 최상단에 위치한 범위
 4. Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)

 ★ 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음


### LEGB Rule 예시
- sum이라는 이름을 global scope에서 사용하게 되면서 기존에 built-in scope에 있던 내장함수 sum을 사용하지 못하게 됨
- sum을 참조 시 LEGB Rule에 따라 global에서 먼저 찾기 때문

```bash
a = 1
b = 2 

def enclosed():
    a=10
    c=3

    def local(c): # local 함수 정의-*
        print(a,b,c)    # 10 2 500-*

    local(500) # 호출된 시점에 500-*
    print(a, b, c)   # 10 2 3     얘는 enclosed()에서 호출됨 a는 10, b를 찾앗더니 없어서 global로 올라가ㅓ서 2 가져오고 c는 3이 있어서 3

enclosed()
print(a, b)  # 1 2

```


## global 키워드
> 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
```bash
num = 0 # 전역 변수

def increment():
    global num # num 을 전역 변수로 선언
    num += 1

print(num)  # 0
increment()
print(num) # 1  #이렇게 전역변수를 함수에서 수정할 수 있게 됨

```

```bash
global_var = '글로벌 값'

def update_value(global_var): # 매개변수
    print(global_var, '매개 변수로 받은 값')
    result = global_var * 3  # 글로벌 변수가 가지고 있던 값 활용 가능
    global_var = '로컬 값'  # 글로벌 변수에 할당된 값에 영향 없이 다른값 재할당 가능
    return result

print(update_value(global_var)) # 인자로  global scope변수를 넘김
print(global_var)

글로벌 값 매개 변수로 받은 값
글로벌 값글로벌 값글로벌 값
글로벌 값

```


### global 키워드 주의사항  
```bash
# 1. 키워드 선언도 하지 않고 하면 안됨
num = 0
 
def increment():
    # 키워드 선언도 하지 않고 하면 안됨

    print(num)
    global num
    num +=1

# 2. 매개변수에 global 사용 불가

```


> global키워드는 가급적 사용하지 않는 것을 권장
- 함수로 값을 바꾸고자 한다면 항상 인자로 넘기고 함수의 반환 값을 사용하는 것을 권장함!

## 재귀 함수 
> 함수 내부에서 자기 자신을 호출하는 함수

### 특징
- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성(점화식: 점점 줄어드는 식 ex. 피보나치 수열)

### 예시 - 팩토리얼 n!
- factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
- 재귀 호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함
- 재귀 호출의 결과를 이용해 문제를 작은 단위의 문제로 분할하고, 분할된 문제들의 결과를 조합하여 최종 결과를 도출
- 무한 호출에 걸릴 위험 !!! ★
1. 종료 조건을 명확히
2. 반복되는 호출이 종료 조건을 향하도록

```bash
def factorial(n):
    # print(n) # 반복되는 과정
    # 종료 조건 : n이 0이면 1을 반환
    if n==0:
        return 1
    # 재귀 호출 : n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n-1)

# 팩토리얼 계산 예시
result = factorial(5)
print(result) # 120

```

## 유용한 함수
### 1. 내장함수
### map(function ,iterable)
 > 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

 ```bash
 numbers = [1,2,3]
 result = map(str, numbers)

print(result) # <map object at >
print(list(result)) # ['1','2','3']


# 참고
import sys
sys.stdin = open('input.txt')

[참고](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline#-input%EB%8C%80%EC%8B%A0-sysstdinreadline%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EC%9D%B4%EC%9C%A0)

T = int(input())
K, N, M = map(int, input().split())

 ```

 ### 2. zip(*iterables)
 > 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```bash
# 두 개의 리스트를 딕셔너리로 변환하기



```

### 3. lambda 함수 
> 이름없이 정의되고 사용되는 익명 함수 
> lambda  매개변수: 표현식
- 간단한 연산이나 함수를 한 줄로 표현할 때 사용
- 함수를 매개변수로 전달하는 경우에도 유용하게 활용
- 일회성으로 사용할때

- quetion.py파일 보기

## packing(패킹)
> 여러 개의 값을 하나의 변수에 묶어서 담는 거
- 변수에 담긴 값들은 튜플의 형태로 묶임
- *을 활용한 패킹 : *b는 남은 요소들을 리스트로 패킹하여 할당
```bash```

- print함수에 임의의 가변 인자를 작성할 수 있었던 이유

## 언패킹
> 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것
- *는 리스트의 요소를 언패킹
```bash 
names = 
```
- **는 딕셔너리 키-값 쌍을 함수의 키워드 인자로 언패킹

# 모듈
> 한 파일로 묶인 변수와 함수의 모음 특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)

### 모듈 가져오기 
> 모듈 내 변수와 함수에 접근하려면 import문이 필요
- 내장함수 help를 통해 모듈에 무엇이 들어있는지 확인 가능
- '.(dot)'은 점의 왼쪽 객체에서 "점의 오른쪽 이름을 찾아라" 라는 의미의 연산자
- from 절을 활용해 특정 모듈을 미리 참조하고 어떤 요소를 import 할지 명시


## 패키지
> 관련된 모듈들을 하나의 디렉토리에 모아 놓은 곳

as : 별명
