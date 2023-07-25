# 비시퀀스 데이터 구조
## Set메서드
> set = 중복 X/ 집합연산에 사용 / 고유한 항목들이 정렬되지 않은 컬렉션
- 고유한 항목들의 정렬되지 않은 컬렉션

### 1. add(x) 
> 세트s에 항목x를 추가. 이미 x가 있다면 변화 없음
```bash
$ my_set = {1,2,3}
my_set.add(4)
print(my_set) # {1,2,3,4}


```

### 2. clear()
```bash
#빈세트는 딕셔너리랑 구분하기 위해서 set()
$ my_set = {1,2,3}
my_set.clear()
print(my_set) # set()
```


### 3. remove(x)
> 세트 s에서 항목x를 제거. 항목x가 없을 경우 Key error
```bash
$ my_set = {1,2,3}
my_set.remove(2)
print(my_set) #{1,3}

my_set.remove(10)  # error

```

### 4. pop()
> 세트 s에서 랜덤하게 항목을 반환, 해당 항목을 제거 
- 리스트에서의 pop이랑 다름
- 세트에서 '임의의' 요소를 제거하고 '반환' <= set 는 순서가 없기 때문에!! ★★

- 실행할 때마다 다른 요소를 얻는다는 의미에서의 '무작위'가 아니라 
- "임의"라는 의미에서 '무작위'
- 해시 테이블에 저장되어있는 순서는 있다. (하지만 우리는 그 순서를 모름)
> 정수 값 자체가 곧 해시 값 (정수는 해쉬값이 정해져있다)(같은 정수는 항상 같은 해시 값을 가진다)
- 문자열은 실행될때 마다 다른 해쉬값을 갖게 된다. -> 실행시마다 다름!(문자열은 가변적인 길이를 갖고 있어서 각 문자들의 유니코드 코드 포인트 등을 기반으로 해시 값을 계산 / 문자열의 내용에 따라 다르게 계산됨)


```bash
$ my_set = {1,2,3}
element = my_set.pop()

print(element) # 1
print(my_set) # {2,3}

```

# 해시 테이블(Hash Table)
- 데이터를 효율적으로 저장하고 검색하기 위해 사용되는 자료구조
- 키-값 쌍을 연결하여 저장하는 방식
- 키를 해시 함수를 통해 해시 값으로 변환하고, 이 해시 값을 인덱스로 사용하여 데이터를 저장하거나 검색
- 이렇게 하면 데이터의 검색이 매우 빠르게 이루어짐
- 파이썬에서 세트의 요소와 딕셔너리의 키는 해시 테이블을 이용하여 중복되지 않는 고유한 값을 저장 
- 세트 내의 각 요소는 해시 함수를


### 5. discard(X)
> remove와 달리 없는걸 삭제하려고 해도 에러가 없음
```bash
$ my_set = {1,2,3}
my_set.discard(2)
print(my_set) #{1,3}

my_set.discard(10) # error 발생 안함
print(my_set.discard(10)) # None
```

### 6. update(iterable)
> 세트 s에 다른 iterable 요소를 추가

```bash
$ my_set = {1,2,3}
my_set.update([4,5,1])
print(my_set) # {1,2,3,4,5} # 중복된 1은 없어짐

```

## set의 집합 메서드
### set1.difference(set2) == set1 - set2(차집합)
> set1에는 들어있지만 Set2에는 없는 항목으로 세트 생성후 반환
```bash



```


### set1.intersection(set2) == set1 & set2
> set1와 Set2에는 모두 들어있는 항목으로 세트 생성후 반환
```bash



```


### set1.issubset(set2) == set1 <= set2
>  set1의 항목이 모두 Set2에들어 있으면 True를 반환
```bash



```


### set1.issuperset(set2) == set1 >= set2
> > set1 또는 Set2에 (혹은 둘다) 들어있는 항목으로 세트를 생성 후 반환

```bash
# set에다가 100 99 같은거 넣어서 실행시켜보자!
set = {0,1,2,3,4}



```


### set1.union(set2) == set1 | set2
> set1에는 들어있지만 Set2에는 없는 항목으로 세트 생성후 반환

## dictinoary 메서드(고유한 항목들의 정렬되지 않은 컬렉션)
### 1. clear()
```bash



```

### 2. get(k [, default])
> 키 연결된 값을 반환하거나 키가 없으면 None 혹은 기본값을 반환
- get() = 메서드임 | 함수임 
- 함수 반환할 값이 없으면  None 반환함

```bash
my_dict = {
  'name': 'Alice'
  'age': 25
}
print(my_dict['name'])
print(my_dict.get('name'))

# 찾고자 하는 키가 없을 때
print(my_dict['age'])     # KeyError
print(my_dict.get('age')) # None
print(my_dict.get('age', 'Unknown')) # Unknown

```

### 3. get(k,v)
```bash



```

### 4. keys() /  values() / items()

```bash
dict_keys(['name','age'])
print(person.keys())
for key in person.keys():
  print(key)

print(person.values())
for value in person.values():
  print(value)

print(person.items())
for key, value in person.items():
  print(key, value)
  
```

### 5. pop(k[,default])
```bash

# key를 제거해버리면 값은 남아있나?
person = {'name':'Alice', 'age':25}
print(person.pop('age'))
print(person) # 같이 없어지네

```
### 6. setdefault(k[,default])
> 키와 연결된 값을 반환까지는 get과 같음 / 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환

```bash
person = {'name':'Alice', 'age':25}

print(person.setdefault('country','KOREA'))

print(person.setdefault('age', 50))
print(person)

```
### 7. setdefault(k,v)
```bash



```
### 8. update([other])
> other가 제공하는 키/값 쌍으로 딕셔너리를 갱신 / 마지막으로 들어간 것으로 기존 키는 덮어씌워짐

```bash
person = {'name':'Alice', 'age':25}
other_person = {'name':'Jane', 'gender':'Female'}

person.update(oter_person)
print(person)

person.update(age=50)
print(person)

person.update(country="KOREA")
print(person)

person.update(age=50, country="KOREA")
print(person)

```

# 나 이거 모르겠음
```bash
# 혈액형 인원수 세기
# 결과 => {'A':3,'B':4, '0':4, 'AB':3}
blood_types =['A','B','A','O','AB','AB','O','A','B','O','B','O','B','AB']


# 1. []으로 풀기
new_dict ={}
# blood_types을 순회하면서
for blood_type in blood_types:
                                   # 기존에 키가 이미 존재한다면,
    if blood_type in new_dict:
                                    # 기존에 키의 값을 +1 증가
        new_dict[blood_type] += 1
        
    # 키가 존재하지 않는다면(처음 설정되는 키)
    else:
        new_dict[blood_type] = 1
         # blood_type에서 나온 'A'를 key로 하고 거기에 값을 1로 준다.
print(new_dict)

# 2. .get()으로 풀기
new_dict ={}
# blood_types을 순회하면서
for blood_type in blood_types:
    
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
    # # 기존에 키가 이미 존재한다면,
    # if blood_type in new_dict:
    #     # 기존에 키의 값을 +1 증가
    #     new_dict[blood_type] += 1       
    # # 키가 존재하지 않는다면(처음 설정되는 키)
    # else:
    #     new_dict[blood_type] =1
print(new_dict)


# .setdefault()
new_dict ={}
for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1
print(new_dict)
```

## 복사
파이썬에서는 데이터의 분류에 따라 복사가 달라짐
'변경 가능한 데이터 타입'/ '변경 불가능한 데이터 타입'

### 복사 유형
1. 할당 
> 할당 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사

2. 얕은 복사
> 슬라이싱을 통해 생성된 객체는 원본 객체와 독립적으로 존재

3. 깊은 복사
> 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함.


```bash
a = [1,2,3]

# 슬라이싱
b = a[:]
b[0] = 100

print(a,b)

# copy
c = a.copy()
c[0] = 100
print(a,c)


# 얕은 복사의 한계
a = [1,2,[1,2]]    # 리스트 안에 리스트(단계가 깊어졌음)
b = a[:]
b[2][0] = 999
print(a,b)  # 위에서는 b만 바꼈었는데 지금은 a도 바뀌어버림!!


a = [1,2,[1,2]]
c = a.copy()    # copy를 해도 그렇다.
c[2][0] = 999
print(a,c)

# 세번째 리스트에서 같은 주소를 참고하고 있어서 그렇다(복사 되다가 말았음)

# 깊은 복사
import copy  # 모듈 제공해줌
original_list = [1,2,[1,2]]

deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 999
print(original_list, deep_copied_list)  
# 이렇게 하면 원본리스트는 바뀌지 않음
```

## 해시 & 메모리
- 해시 테이블 : 자료구조를 만들어둔 것
- 이 자료구조가 메모리에 저장됨
