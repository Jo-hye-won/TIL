원격저장소에 있는 애랑 로컬에서 작업하고 있는 애랑 같은 깃폴더에 있는걸로 관리


★★★ git push origin master 하면 나의 github에 올라간다!! ★★★

### 원격 저장소에 업로드
```bash
$ git remote add{remote_nickname}{remote_url}
# git remote add origin {내 깃허브 주소}
```

## 원격 저장소에 저장
```bash
$ git pusth origin master
```

## 집가서 다운받는 방법(최초로 내려받을 때)
다운받을 파일에서 vs코드 열어서 터미널에
```bash
$ git clone {주소복사:repository_url}
```

## 이미 깃을 가지고 있고 원격 저장소에 대한 정보도 가지고 있을 경우 내려받으려면?
```bash
$ git pull origin master
```