# 제어문(조건문, 반복문)
> 코드의 실행 흐름을 제어하는 데 사용되는 구문
- '조건'에 따라 코드 블록을 실행하거나 또는 실행하지 않거나  '반복'적으로 코드를 실행

## 1. 조건문
> 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

### if/elif/else
> 파이썬 조건문에 사용되는 키워드
- 제일 위에 범용성이 큰거 넣어야 함

### if statement의 기본 구조
- 구조

```bash
if 표현식:
   코드블록
elif 표현식:
    코드블록
else: # 표현식 존재하지 않음 / 위의 모든 case가 아닌 경우
    코드블록

 
a=5
if a>3:
  print('3초과')
else
  print('3이하')

print(a)
# 앞의 코드블럭에서 True가 나오면 else부분은 패스가 되고 print로 간다.

# a=3이라서 앞의 표현식이 False 가 나오면 else로 가서 print(a)가 동작함

```

#### 복수 조건문
> 조건식을 동시에 검사하는 것이 아니라 순차적으로 비교
위에서부터 차례차례 검사하면서 내려옴!
```bash 
dust = 35
if dust >150:
  print('매우 나쁨')
elif dust >80:
  print('나쁨')
elif dust > 30:
  print('보통')
else:
  print('좋음')

```

#### 중첩 조건문
> 
```bash 
dust = 480

if dust >150:
  print('매우 나쁨')
  if dust > 300:        # 조건문 추가 가능
    print('위험해요! 나가지 마세요!')
elif dust >80:
  print('나쁨')
elif dust > 30:
  print('보통')
else:
  print('좋음')

```

### 홀수/짝수
```

```

## 2. 반복문
> 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
- 특정 작업을 반복적으로 수행 : 종료 조건이 없음
- 주어진 조건이 참인 동안 반복해서 실행 : 조건이 Flase 면 종료됨(종료조건이 있음)


### for / while
> 파이썬 반복문에 사용되는 키워드

### 1.for
> 임의의 '시퀀스(인덱스, 순서, 길이가 있음-> 개수가 있음)' 항목들을 그 시퀀스에 들어있는 순서대로 반복
- 자체적인 종료조건이 있음 (개수가 있기 때문에)(길이가 있는 애를 반복하는 거다.)

- 기본 구조
```bash
for 변수 in 반복 가능한 객체:
    코드 블록
```
- 반복 가능한 객체 (iterable)
> 반복문에서 순회할 수 있는 객체(시퀀스 객체 뿐만 아니라 dict, set등도 포함)
- 반복 불가능한것 : 정수

### for문 원리
- 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록이 실행
- 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드블록이 다시 실행
- ... 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행
```bash
items = ['apple', 'banana',  'coconut']

country = 'Korea' #  문자열 순회
for i in range(5) # range 순회
```

### 인덱스로 리스트 순회 
> 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기
```bash
numbers = [4, 6, 10, -8, 5]
for i in range(len(numbers)):
  numbers[i] = numbers[i] * 2

print(numbers)
```

### 중첩된 반복문
```bash
outhers = ['A','B']
inners = ['c','d']

for outer in outers:    # outer로 올라간다.
  for inner in inners:  # inner의 반복이 다 끝나야 
    print(outer, inner)

# A,c -> A,d -> B,c -> B,d
```
- print가 호출되는 횟수 -> len(outers) * len(inners)
- 안쪽 반복문은 outers 리스트의 각 항목에 대해 한 번씩 실행됨

### 중첩 리스트 순회
> 안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회
```bash
elements = [['A','B'], ['c','d']]
for elem in elements:
  for item in elem:
    print(item)
# A B c d
```


### 2. while(조건이 참일동안 계속 반복)
> 주어진 조건식이 참인 동안 코드를 반복해서 실행 == 조건이 거짓이 될 때까지 반복

- 기본구조
while 조건식:
    코드블록
  
```bash
a = 0

while a < 3:
    print(a)
    a += 1      # 종료조건을 만들어두지 않으면 무한반복됨

print('끝')

# 0 1 2 끝
```

#### 사용자 입력에 따른 반복
> while문을 사용한 특정 입력 값에 대한 종료 조건 활용하기

```bash
주피터 노트북?

number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:  # 0보다 큰 수가 들어와야 종료됨
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    
    number = int(input('양의 정수를 입력해주세요.: '))  # 다시 while로 넘어감

print('잘했습니다!')

# 양의 정수를 입력해주세요.: 0
# 0은 양의 정수가 아닙니다.
# 양의 정수를 입력해주세요.: -1
# 음수를 입력했습니다.
# 양의 정수를 입력해주세요.: 1
# 잘했습니다!
```

- while문은 반드시 종료 조건이 필요!!
> for = iterable의 요소를 하나씩 순회하며 반복
  while = 주어진 조건식이 참인 동안 반복


### 적절한 반복문 활용하기 
#### for
- 반복 횟수가 명확하게 정해져 있는 경우에 유용
- 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때

#### while
- 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 대 유용
- 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때가지 반복하는 경우

### 반복 제어
> for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만 때떄로 일부만 실행하는 것이 필요할 때가 있음
- break : 반복을 즉시 중지
- continue : 다음 반복으로 건너뜀


```bash
# 프로그램 종료 조건 만들기

number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break
    else:
        print('0은 양의 정수가 아닙니다.')
    
    number = int(input('양의 정수를 입력해주세요.: '))  # 다시 while로 넘어감

print('잘했습니다!')

```

```bash
# 짝수 찾으면 종료

numbers = [1, 3,5,6,7,9,10,11]
found_even = False

for num in numbers:
    if num % 2 == 0:
      print('첫 번째 짝술ㄹ 찾았습니다: ', num)
      found_even = True
      break
  
if not found_even:
  print('짝수를 찾지 못했습니다.') 


### 리스트에서 홀수만 출력하기
# 현재 반복문의 남은 코드를 건너뛰고 '다음 반복'으로 넘어감 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fr num in numbers:
    if num % 2 == 0:
          continue
       print(num)

```
- break와 continue를 남용하는 것은 코드의 가독성을 저하시킬 수 있음
- 특정 종료 조건을 만들어  break을 대신하거나, if문을 사용해 continue처럼 코드를 건너 뛸 수도 있음
- 약간의 시간이 들더라도 가능한 코드의 가독성을 유지하고, 코드의 의도를 명확하게 작성하도록 노력하는 것이 중요


## List Comprehension
> 간결하고 효율적인 ★리스트 생성 방법★

### 구조
```bash
[expression for 변수 in iterable]
[expression for 변수 in iterable if 조건식]

list(expression for 변수 in iterable) # <- 리스트 함수

```

### 활용
```bash
# 0-9 요소를 가지는 리스트 만들기
# 1. 일반적인 방법
new_list = []
for i in range(10):
    if i % 2 == 1:  #  홀수만 나오게 조건 추가
         new_list.append(i)

print(new_list)

# 2. list comprehension
new_list_2 = [i for i in range(10) if i % 2 == 1]  #  홀수만 나오게 조건 추가
print(new_list_2)


# if else 사용 가능(앞에 적어야함) / elif 사용 불가능 / 중첩 if는 가능
new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)] 

```
## 리스트를 생성하는 3가지 방법 비교

- 정수 1,2,3을 가지는 새로운 리스트 만들기


```bash

numbers = ['1', '2', '3']

# 1. for loop 
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)  # [1, 2, 3]

# 2. map사용
new_numbers_2 = list(map(int, numbers))
print(new_numbers_2)    # [1, 2, 3]

# 3. list comprehension
new_numbers_3 = [int(number) for number in numbers]
print(new_numbers_3)

```

## pass
> 아무런 동작도 수행하지 않고 넘어가는 역할 
- 문법적으로 문장이 필요하지만 프로그램 실행에는 영향을 주지 않아야 할 때 사용

### 1. 코드 작성 중 미완성 부분
 - 구현해야 할 부분이 나중에 추가될 수 있고, 코드를 컴파일하는 동안 오류가 발생하지 않음
 
 ```bash
 def my_funcion():
    pass
 ```

### 2. 조건문에서 아무런 동작을 수행하지 않아야 할 때
```bash
if condition:
    pass  # 아무런 동작도 수행하지 않음
else:
    # 다른 동작 수행

```

### 3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법
```bash
while True:


```

## enumerate(iterable, start=0)
> iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
```bash
# enumerate
result = ['a', 'b', 'c']

print(enumerate(result)) # <enumerate object at 0x000001E6D63A0F80>
print(list(enumerate(result))) # 요소 하나하나가 튜플로 되어있음, 인덱스와 함께 있음

for index, element in enumerate(result):
    print(index, element, end =" ")

```



# 관통 프로젝트
- 11시 ~ 6시까지 만드는 것 (한주동안 배운거 가지고 함)
- 마감 기한에 맞춰서 작동이라도 하게 만든다.
- 코드 완성보다 README 작성에 집중 
    -> 오늘 못푼거, 오늘 해결하느라 고생한 것
- 10번 만든다
- 완전 마지막 주 한주에는 일주일 반동안 관통 프로젝트함
