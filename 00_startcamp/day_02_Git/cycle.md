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

