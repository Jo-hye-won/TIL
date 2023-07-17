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

## 파일 안에 있는거 다 커밋하려면
```bash
$ git add . 
 # 여기서 . 은 현재파일을 말한다
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


> ★★★★
정리 : add로 staging area에 추가하고 나서 repository에 저장하고나서 git log로 기록 확인하기!
                                                                              ★★★★


### 오타있게 커밋했기 때문에 수정을 하고 싶다!(직전커밋수정)
```bash
git commit --amend   # amend : 개정하다
# vim에서 커밋 내용 수정하기
```
1. 삽입가능(수정가능)한 상태로 만들어야 함 : insert 키 누르기
2. 커밋 메시지 수정하기
3. Esc로 수정끝났음을 알리기(삽입 상태 종료)
4. :wq 입력해서 저장하고 종료(write quit의 의미)
5. 나와서 git log 확인하면 수정되어 있음


>(use "git restore <file>..." to discard changes in working directory) :
워킹디렉토리에서 발생한 변경사항을 없애는 친구 : 마지막 변동사항에서 추가 변동사항을 없애서 최신 저장되었던 상태로 돌아가는 것!



- cd ~ 으로 파일이동하기~~
> 방향키로 움직이면 log 다 볼 수 있음
-> log에서 나가려면 q 누르면 나가진다~~~

github와 gitlab = remote repository(원격저장소)



### git 설정 초기화
```bash
# vim을 활용해서 설정 제거하기
# vim git 설정 파일 열기
$ vim ~/.gitconfig
# inser 키 : 수정 상태 만들기
# --insert-- 인 상태에서 모든 내용 삭제
# esc: 수정 상태 종료
# :wq
```

- code ~/.gitconfig : vscode에서 수정하기

```bash
$ git log --oneline
# log를 하나의 라인으로 보여주세요
```

# Cycle

1. 폴더 만들기
2. touch README.md   로 파일 만들 수도 있음
3. git add README.md
4. git commit -m " 이름적고 "

5. 새 레포지터리 만들어서 이름 정하고 : 이건 깃허브에서

6. git init 후 -> 
    git remote add origin {복사한 레포지터리경로}
7. git push origin master 로 깃에 올리기
8. 잘올라갔는지 확인하기

### 하나 더 만드려면?
git remote add origin 하면 이미 있는 이름
git remote add second로 새로운 이름 만들기
git push second master
레포지터리 여러개 만들어서 여러군데 올릴 수 있는 것!

원격저장소에 있는 애랑 로컬에서 작업하고 있는 애랑 같은 깃폴더에 있는걸로 관리

★★★ git push origin(리모트 닉네임) master 하면 나의 github에 올라간다!! ★★★

### 원격 저장소에 업로드
```bash
$ git remote add{remote_nickname}{remote_url}
# git remote add origin {내 깃허브 주소}
```
git remote remove origin -> 주소 잘못 설정했을 때 지우는 것

### 원격 저장소에 저장
```bash
$ git push origin master
```

### 집가서 다운받는 방법(최초로 내려받을 때)
다운받을 파일에서 vs코드 열어서 터미널에
```bash
$ git clone {주소복사:repository_url}
```

### 이미 깃을 가지고 있고 원격 저장소에 대한 정보도 가지고 있을 경우 내려받으려면?
```bash
$ git pull origin master
```


