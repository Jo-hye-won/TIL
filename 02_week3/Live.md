## 데이터 구조
> 여러 데이터를 효과적으로 사용, 관리하기 위한 구조(str, list, dict 등)

### 데이터 구조 활용 
> 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 '메서드를 호출'하여 다양한 기능을 활용하기


### 메서드(method)
> 객체에 속한 함수 : 객체의 상태를 조작하거나 동작을 수행
- 지금까지 썼던 함수들이랑 위치가 다름

### 메서드 특징
- 메서드는 클래스(class) 내부에 정의되는 함수
- 클래스는 파이썬에서 '타입을 표현하는 방법'이다.
- 예를들어 help함수를 통해 str을 호출해보면 clas였다는 것을 확인 가능
- 어딘가(클래스)에 속해 있는 함수이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재 


> 월말평가는 vscode에서 풀이 해야 함

#### print(help(list))
class list(object)
 |  list(iterable=(), /) 변경가능함
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified. 구체적으로 인자를 넣으려면 반복가능한 객체가 여기의 인자로 들어가야 한다.
 |
 |  Methods defined here: 여기서부터는 메서드가 정의되어있습니다.
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return key in self. 
 |
 |  append(self, object, /)
 |      Append object to the end of the list. 리스트의 마지막에 추가한다.

 > 키보드에서 q 누르면 나가진다.

### 메서드 호출 방법
    데이터 타입 객체.메서드()
 ex)        'hello'.capitalize() # 첫번째 문자가 대문자이고 나머지는 소문자로 된 문자열의 '복사본'을 반환함 => 원본은 그대로 있음. 


 ## 시퀀스 데이터 구조
> 시퀀스 타입 -> 정렬이 아니고 순서! 순서가 있음.

### 문자열 조회/탐색 및 검증 메서드
> s = 문자열

- s.find(x) : x의 첫번째 위치를 반환. 없으면 -1 을 반환

```bash
$ print('banana'.find('a')) # 1
$ print('banana'.find('z')) # -1 
```

- s.index(X) : x의 첫 번째 위치를 반환. 없으면 오류 발생

```bash
$ print('banana'.find('a')) # 1
$ print('banana'.find('z')) # ValueError : substring not found : 코드가 이 이후로 아직 진행되지 못하고 있다는 것. 코드가 중단됨. 
```
- s.isalpha() : 알파벳 문자 여부 * 단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함)

```bash
$ string1 = 'Hello'
$ string2 = '123'
$ print(string1.isalpha()) # True
$ print(string2.isalpha()) # False
```
- s.isupper() : 대문자 여부 
- s.islower() : 소문자 여부
- s.istitle() : 타이틀 형식 여부
> 문자열이 제목이 있는 문자열이고 적어도 하나의 문자가 있는 경우 True 반환
예를 들어 대문자는 대소문자가 없는 문자 뒤에만 올 수 있고 소문자는 대소문자만 뒤따를 수 있습니다. 그렇지 않으면 False 반환

> python documentation => 공식문서 => 자습서, 라이브러리 레퍼런스

### 문자열 조작 메서드(새 문자열 반환)
> 여기 있는 메서드를 젤 많이 사용할 것임

### 1.s.replace(old,new[,count]) 
- 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 
- [] 안에 있는건 선택인자 <- 파이썬 문법이 아님! -  ebnf 표기법(추가 규칙)
- 필수인자는 2개 (old, new)
- [,count]

### 2. .strip ([chars]) 
> 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거

### 3. .split(sep=None, maxsplit = -1) ★★★
> 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환

### 4. 'seperator'.join([iterable]) ★★★
> iterable 요소들을 원래의 문자열을 구분자로 이용하여 하나의 문자열로 연결
- 다른 메서드들과 다르게 seperator이 괄호안에 있지 않고 앞에 나와있음.

### 5. .capitalize / title / upper / swapcase()



>  메서드는 이어서 사용 가능!! (chained한다고 함)


## 리스트 ★★★★

### 리스트 값 추가 및 삭제 메서드
- L.append(x) : 리스트 마지막에 항목 x를 추가 ★
- L.extend(iterable) : 리스트에 다른 반복 가능한 객체의 모든 항목을 추가★

```bash 
# extend와 append의 차이

numbers = [1,2,3]
numbers2 = [4,5,6]

numbers.append(numbers2)
print(numbers)             # [1, 2, 3, [4, 5, 6]]

numbers.extend(numbers2)
print(numbers)            # [1, 2, 3, 4, 5, 6]
``` 

- insert(i,x) : 리스트의 지정한 인덱스 i 위치에 항목 x를 삽입

- remove(x) : 리스트에서 '첫 번째로 일치하는' 항목을 삭제

#### pop(i) ★★★
> 리스트에서 지정한 인덱스의 항목을 제거하고 '반환' 
- 작성하지 않을 경우 마지막 항목을 제거

```bash
my_list = [1,2,3,4,5]

item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)  #5
print(item2)  #1
print(my_list) #[2,3,4]

```


- clear() : 리스트의 모든 항목을 삭제 => 빈 리스트가 된다


### 리스트 탐색 및 정렬 메서드

#### 1. index(x, start, end)
> 리스트에서 첫번째로 일치하는 항목의 '인덱스'를 반환

#### 2. reverse() ★
> 리스트의 순서를 역순으로 변경(정렬 X)
- 뒤집는 것이지 정렬이 아니다!!!!
- 역순으로 정렬하는 것이다(X)

#### 3. sort() ★
> '원본' 리스트를 오름차순으로 정렬 
- 복사본을 주는 것이 아니다. 반환이 없다.(원본을 바꾼다)
- 어떠한 변수에 할당하고 있지 않다. 
- 기본인자가 reverse = False 이다.
- sort(reverse=True)로 기본인자를 바꿔주면 내림차순으로 정렬된다.

### sort와 sorted 
```bash
numbers = [3,2,1]

# sort 메서드 
# print(umbers.sort())  # None -> 복사본을 만들지 않았다. 반환이 없다. 원본을 바꿈

# sorted 함수
print(sorted(numbers)) # [1,2.3] -> 반환이 있다. 원본은 바뀌지 않았다. 
print(numbers)  # [3,2,1]



# 과제 2번 #
def find_min_max(nums):
    # my_list = nums.sort() # 원본을 정렬하는 거라서 변수할당할 필요 없음
    nums.sort()
    min = nums[0]
    max = nums[-1]
    # my_tuple = ','.join(min,max)
    return (min, max)

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)

```


#### 4. count(x)
> 리스트에서 항목 x가 등장하는 횟수를 반환


### 문자열에 포함된 문자들의 유형을 판별하는 메서드
- isdecimal() : 문자열이 모두 숫자문자(0~9)로만 이루어져 있어야 True
- isdigit() : isdecimal()과 비슷하지만, 유니코드 숫자도 인식 ('①'도 숫자로 인식)
- isnumeric() : isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식(분수, 지수, 루트 기호도 숫자로 인식)

> isdecimal() <= isdigit() <= isnumeric()


### copy

```bash 
numbers = [1,2,3]

# 1. 할당
list1 = numbers

# 2. 슬라이싱  -> 복사본을 만든 것이라서 겉보기에는 똑같지만 애초에 다른 주소가지고 있음
list2 = numbers[:]

# 3.
numbers[0] = 100   # 원본의 0번째가 바라보고 있는 방향이 100으로 바뀜(불변타입이라서 값이 바뀌는게 아니라 바라보는 주소가 바뀌는 것)

print(list1)  # [100,2,3] -> 원본에 따라서 바뀜
print(list2)  # [1,2,3] -> 애초에 겉보기만 같고 실제 주소는 아예 다른 방에 들어있는 리스트였기에 그대로이다. 

```


