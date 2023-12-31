## 앞으로 일정
> 월요일 시험 종류 2개
- 1시간(과목평가)있을 때
= 라이브강의 10시-12시

- 2시간(월말평가)있을 때
= 오후에 라이브 강의
> 금요일 = 관통 PJT하는 날

##
파이썬강의(2주) -> 알고리즘 바로 이어짐(5주-6주) : 검정시험도 볼 것 -> Web(thml/css) -> 백앤드 -> 자바스크립트 -> 프론트앤드,프래임워크(django) 순서로 진행 될 것
##

### 프로그래밍?
- 프로그램 = 명령어들의 집합
- 핵심 : 새 연산을 정의하고 조합해 유용한 작업을 수행하는 것 -> '문제를 해결'하는 매우 강력한 방법
문제를 해결하기 위한 도구가 프로그래밍 언어들이다~!

- 프로그래밍 언어 : 컴퓨터에게 작업을 지시하고 문제를 해결하는 도구/ 컴퓨터와 소통하기 위한 도구

## 파이썬
- jetbrain survey : 파이참 만든 곳
- 사람에 가까운 문법을 가지고 있다.
- 응용분야 : 데이터 분석, 인공지능, 웹 개발, 자동화 등
- 커뮤니티의 기반이 있어야 언어가 살아남을 수 있음. 세계적인 규모의 풍부한 온라인 포럼 및 커뮤니티 생태계있음. 파이콘이라는 매년 열리는 행사도 있음. 

### 파이썬 프로그램이 실행되는 법 
-  컴퓨터는 기계어로 소통하기 떄문에 사람이 기계어를 직접 작성하기 어려움
- 인터프리터가 사용자의 명령어를 운영체제가 이해하는 언어로 바꿈

### 인터프리터 사용하는 방법
1. shell프로그램 이용 : 한번에 한 명령어씩 입력해서 실행
- git bash 열어서
```bash
 $ python -i
  # i는 인터프리터를 뜻함
```
저 상태에서 입력하면 바로바로 한명령어씩 실행됨 
- exit()로 나갈 수 있음
- ctrl + c를 연타해도 됨

2. 확장자 .py인 파일 작성

## 표현식과 값
1+2 : 하나의 '표현식'
- 표현식 : 값, 변수, 연산자 등을 조합하여 계산되고 결과를 내는 코드 구조/
표현식이 '평가'되어 값이 반환됨
 
    : 그냥 값 하나도 표현식

- 평가(Evaluate) : 표현식이나 문장을 순차적으로 평가하여 프로그램의 동자가을 결정함
ex) hi 가 올바른값인지 평가 후 greeting 에 할당함

- 문장(Statement) : 실행가능한 동작을 기술하는 코드 (조건문, 반복문, 함수 정의 등) 

### 표현식과 문장
: 문장은 표현식(Expression) 중에서도 그 자체만으로 실행이 가능해야 함!
실행이 되지 않으면 그냥 표현식

: 문장은 보통 여러개의 표현식을 포함
: 모든 표현식은 문장이다. 
반면에 어떤 문장은 표현식이 아니다.

### f'string
문자열 안에 표현식을 집어넣고 쓸 수 있음.


## 타입
> 값이 어떤 종류의 데이터인지, 어떻게 해석되고 처리되어야 하는지를 정의

- 2가지 요소로 이루어짐
- '값(피연산자)'과 '값에 적용할 수 있는 연산'

### 데이터 타입
- Numeric Type : int(정수), float(실수) , complex(복소수) : 단일 데이터들
- (Sequence)시퀀스 타입 : list, tuple, range : 순서가 있는 데이터들
- text 시퀀스 타입 : str(문자열): 순서가 있음 'Hello'의 하나하나가 순서가 있고 인덱스에 넣어서 하나하나 조회할 수 있다는 뜻
- set types : 집합의 연산을 할 수 있음
- Mapping Types(매핑타입) : dict : key-value 형태로 되어있는 것 : 데이터 다룰 때 자주 사용할 것(데이터 받아오거나 만들거나 할 때)
- 기타 : None(값이 없음을 의미), Boolean(True/False), Function

## 산술 연산자
-  / : 나눗셈
- // : 정수 나눗셈(몫)
-  % : 나머지
- ** : 지수(거듭제곱)

### 연산자 우선순위 ★★
> **(지수) -> -(음수 부호) -> *, /, //, % -> +,-(덧셈, 뺄셈)
- -(2**4) = -16
- ★ -2 **4 = -16 (지수가 우선순위라서 지수먼저 계산을 끝낸 후에 -부호가 붙기 때문에 -16이 된다) ★
- (-2)**4 = 16 (이렇게해야 -2의 4제곱을 해줄 수 있음)


## 변수와 메모리 "값이 저장되는 법"
### 변수
- 값을 참조하는 이름 
- 참조 : 무언가(어떤 값)를 바라보고 있다
- 할당문
```bash
$ degrees = 36.5
# 변수 degrees에 값 36.5를 할당했다.
```

### 변수명(식별자) 규칙
- 영문 알파벳, 언더스코어(_),숫자로 구성
- 숫자로 시작할 수 없음
- 대소문자를 구분
- 아래 키워드는 파이썬을 내부 예약어로 사용할 수 없음 : 예약어는 애초에 색이 다르게 나온다!
> ['Flase', 'None', 'True', 'and', 'as', assert, async, await, class, break, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lamda, nonlocal, not, or, pass, raise, return, try, while, with, yield, __peg_parser__, elif]

### 변수, 값 그리고 메모리
- 거리에 집 주소가 있듯이 메모리의 모든 위치에는 그 위치를 고유하게 식별하는 메모리 주소가 존재
- 값이 주소에 저장 된 다음에 변수에 주소를 할당
- 주소의 닉네임이 변수인 것 변수에 주소가 들어있다.
- 객체(Object) : 타입을 갖는 메모리 주소 내 값 / "값이 들어있는 상자"

- 변수는 그 변수가 참조하는 객체의 메모리 주소를 가짐

### 할당문
variable = expression
1. 할당 연산자(=) 오른쪽에 있는 표현식을 평가해서 값(메모리 주소)을 생성
2. 값의 메모리 주소를 '=' 왼쪽에 있는 변수에 저장

### 변수에 재할당 ★★
```bash
$ number =10
double = 2* number
print(double) # 20

number =5
print(double) #20

# number 가 뭘 보고 있던 double은 계속 20을 보고 있으니까 20이 print된다
```

## 읽기 좋은 코드(Style Guide)
[코드의 일관성과 가독성을 향상시키기 위한 규칙과 권장 사항들의 모음](https://peps.python.org/pep-0008/)

1. 변수명은 무엇을 위한 변수인지 직관적인 이름을 가져야 함(변수의 이름을 보고 뭘 가지는 변수인지 알 수 있도록)
- 'is_'로 시작하는 함수나 변수는 값을 True나 False를 가지고 있는 것을 할당하는 것이 암묵적 룰( is_ -> T/F)
```bash
$ temperature = 25
is_hot = temperature > 30
```

- 단/복수도 알 수있게
```bash
# 시간 예시
# 초 분 시
seconds = 60
minute = 60
hours = 24
# 변하지 않는 고정된 값(상수)들은 대문자로 해주는 게 좋음
#(대문자 -> 상수)
SECONDS_PER_MINUTE = 60
```

2. 공백(spaces) 4칸을 사용하여 코드 블록을 들여쓰기
> tab이랑 spaces랑 원리가 다른데 vscode 에디터가 알아서 처리해주고 있는거다. 
3. 한 줄의 길이는 79자로 제한하며, 길어질 경우 줄 바꿈을 사용
4. 문자와 밑줄(_)을  사용하여 함수, 변수, 속성의 이름을 작성
> snake_case 라고 함
> Pascal Case / camel case 도 있음

5. 함수 정의나 클래스 정의 등의 블록 사이에는 빈 줄을 추가
```bash
$ def simple():
    adhud
    fnuiweofn
# 요 사이를 두 줄 띄우는게 답답해 보이지 않고 구조가 잘 보일 것

def asdasd():
# 연산자 사이도 띄어쓰기 해주는게 보기 편하다!
```
스타일가이드는 이걸 안한다고 실행이 안되거나 하는 것은 아님. 


## 참고
[Python Tutor](https://pythontutor.com) : 중간에 있는거를  render all objects on the heap으로 바꿔서 보기

## 주석
- ctrl + /
- """ """ 사용해서 여러 줄 주석 하는 것은 설명서 쓸 때 사용함


> ★★ 흔들리지 말고 한 가지 언어부터 잘 해두자 ★★

> 내가 원하는 회사에서 사용하는 언어와 툴이 있다. 

> 파이썬으로 알고리즘 푸는 건 다른 언어로 푸는 것보다 조금이라도 유리한 위치에서 시작하는 것이다.

> 우리는 파이썬을 배우고 있지만, 실제로는 프로그래밍 언어에 대한 전반적인 이해력을 기르고 있는 것.