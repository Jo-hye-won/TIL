- project.ssafy = 매일 과제, 실습할 거 보여주는 사이트
- lab.ssafy = github 말고 gitlab임
    과제제출하는곳, 강사님이 코드 올려주는 곳


## 깃랩에 올리기

```bash
$ git push lab master
```
$ git push -u origin master
$ git remote add lab https://lab.ssafy.com/hws9701/til_hw.git

- repository  연동 : github, gitlab
- gitignore : 공유하지 않을 파일 -> db에 사용됨, 가상환경, 개인설정들
 .gitignore 파일 생성(.을 파일이름 앞에 )

 # 과제하는 방법(과제 매일 2개)
 1. 프로젝트싸피에 목차눌러서 들어가기
 1~5단계 실습 + 과제 2개 (과제2개는 풀이 다해줌)
 2. 상세보기
 3. 그냥 바탕화면에서 비에스코드 열어서 git clone {주소} 으로 다운받기 
        -> 다만들어져 있는거 이미 git으로 관리되고 있는 거를 받아오는거라서 내가 git remote add 안해도 되는 것!
 4. code . 으로 vscode야 현재 폴더 열어줘 해가지고 실습하라는거 하고나서 
 5. add . 하고 commit -m 하고  전체 다해서 git push origin master 해서 push하기
 > git으로 변동 사항을 기록: git status-> git add filename.py -> git commit -m commit_message -> git push {저장소 이름}{작업자 이름}: git push origin master
 6. 온라인실습실에서 실행해서 commit 잘 됐는지 확인하고
 7. 과제 제출하기 꼭 누르기!!!!

 # lectures에서는 pull만 받을거다!
 