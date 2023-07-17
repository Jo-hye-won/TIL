## CLI : Command line Interface

- 새 폴더 만들기
```bash
$ mkdir new_folder
# mkdir : make directory
```


- 작업 위치를 new_folder로 이동
```bash
$ cd new_folder
```

- 현재 작업 위치를 열기
```bash
# . -> 상대 경로에서의 현재 위치
$ start .
```

- (내가 지금 있는 위치에서) VS코드를 열어줘
```bash
$ code .
```

- vs코드야 (README)파일을 만들어줘
```bash
$ code README.md
# ctrl+s로 저장
```

- 현재 작업 위치의 파일 목록
```bash
$ ls
# 리스트
```

- 파일의 이름을 바꾸거나 위치를 옮기거나
```bash
$ mv {이동할 대상}{이동될 위치} 
# 위치=디렉토리
$ mv {이름 바꿀 대상}{바꿀 이름}
```


## 상대경로와 절대경로
1. 절대경로 : 컴퓨터의 root부터 시작하는 경로
 - 모든 경로를 다 적어둔거
 - /c/Users/SSAFTY/Desktop/new_folder

2. 상대경로 : 현재 위치를 기준으로 보는 경로
 - 나를 기준을 경로를 지정
 - . -> 현재위치
 - .. -> 상위폴더로 이동

 - 상위 디렉토리로 위치 옮겨가기
```bash
$ cd ..
```



## 삭제(복구 안됨)
```bash
$ rm{파일명}
$ rm -r{폴더}
# 재귀(r) : 본디의 것으로 돌아오는 것
```


## one-dash / double-dash
- one-dash : 명령어 option을 축약된 형태로 입력
- double-dash : 축약된 형태 없이 표준어 그대로 옵션 입력 / 명령어의 직관적인 이해 가능