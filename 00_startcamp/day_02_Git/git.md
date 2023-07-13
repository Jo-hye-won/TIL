# Git 이란..
> 분산 버전 관리 시스템

> 코드의 '변경 이력'을 기록하고 '협업'을 원활하게 하는 도구

```python
print('hello, git!')
```
## git의 역할

- 코드의 버전 관리
- 개발되어 온 과정 파악
- 이전 버전과의 변경 사항 비교




> 버전 관리 : 변화를 기록하고 추적하는 것

### 분산과 중앙집중식
- 분산 : 버전을 여러 개의 복제된 저장소에 저장 및 관리 / 협업편리함 / 충돌상황(conflit) / 병합한다(merge) / 인터넷연결 안되어있어도 작성 가능
<-> 중앙집중식 : 버전은 중앙 서버에 저장, 중앙서버에서 파일을 가져와 다시 중앙에 업로드
- git <> github

- 강의용은 gitlab 사용할 것임!
     개인은 github 쓰면됨

## git의 3가지 영역
1. Working Directory : 실제 작업하고 있는 영역
2. Staging Area : working directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
3. Repository : 버전(commit) 이력과 파일들이 영구적으로 저장되는 영역 / 모든 버전과 변경 이력이 기록됨 / 저장소!
> Repository가 어디있나??

> 버전 => commit 찍으세요 = 변경된 파일 저장하세요


상위폴더 상위폴더로 옮기고 싶다
> cd ../../

## git 초기화(initialize)
```bash
$ git init
```
* 파일 보기에서 숨긴항목, 파일확장명 체크해두기!

> lectures 안에 git만들어둠 : lectures안의 하위항목들을 모두 관리하겠다는 뜻!

> 폴더의 관리주체의 이름이 master 

> git안에 git 만들어서 서브모듈 할 수는 있지만 복잡함

## git 지우기
```bash
$ rm -r .git
```

> 숨김파일 있는지 확인하고 싶으면
```bash
$ ls -a    #a= all의 뜻
```


# Commit
 버전 => commit 찍으세요 = 변경된 파일 저장하세요


자격증명 관리자 -> windows 자격 증명

### 상태 확인 명령
```bash
$ git status  #깃아 너의 상태를 보여줘
```

- 지금 너 마스터로 하고 있는 상태야 아직 커밋이 없어. 아직 깃이 관리하지 않는 파일이 있어. git add를 사용해서 나중에 커밋할때 사용할 수 있게 입력해. 트레킹할 수 있게 만들어라. 변경사항을 기록할 수 있도록! 비어있는 파일이라도 있어야 다음에 뭐가 바뀌었는지 알 수 있잖아. 

### staging area에 추가하기
```bash
$ git add README.md
$ git add {path}<folder_name>/{file_name}
```

git rm : rm 리무브 해줘 cach 캐싱되어있는 정보를 unstage할 수 있도록

### repository 에 저장하기
```bash
$ git commit -m "commit message"
```
  - : 약어


### git 기초설정하기
```bash
$ git config --global user.email "hws9701@naver.com"

$ git config --global user.name "조혜원"

$ git config --global --list
```
git config --global user.email "hws9701@naver.com"
git config --global user.name "조혜원"
git config --global --list 하면 설정 잘했는지 확인할 수있음!

### 터미널에서 복사 붙여넣기
- 복사 : 오른쪽 마우스
- 붙여넣기 : shift + insert

### 커밋 기록 확인하기
```bash
$ git log
```

commit 17c89d5e13d6f818b68b8db717e0ae2bc49c6701 (HEAD -> master) : 커밋 버전을 알려주는 고유값 난수 : 중복될 일이 없다. 
