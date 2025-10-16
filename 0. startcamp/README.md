

📘 CLI & Git 요약 정리

🖥️ CLI (Command Line Interface)

🔹 개념

명령어 기반 인터페이스
마우스 없이 텍스트 명령어로 컴퓨터를 조작하는 방식


🔹 주요 명령어 (Linux 기준)

명령어	설명
```
pwd	현재 경로 출력
ls	현재 폴더의 파일 목록 출력
cd 경로	해당 경로로 이동
cd ..	상위 폴더로 이동
mkdir 폴더명	새 폴더 생성
touch 파일명	빈 파일 생성
rm 파일명	파일 삭제
rm -r 폴더명	폴더 삭제
mv 파일A 파일B	파일 이동 or 이름 변경
clear	터미널 화면 정리
```


---

🗃️ Git

🔹 개념

분산 버전 관리 시스템 (DVCS)

코드 변경 이력 추적, 복원, 협업 가능


🔹 Git vs GitHub

Git: 로컬에서 버전 관리 도구

GitHub: Git 저장소를 저장/공유하는 웹 플랫폼 (원격 저장소)



---

🔹 Git 기본 흐름
```
git init                # Git 저장소 생성
git status              # 현재 상태 확인
git add 파일명          # 변경 파일 스테이징
git commit -m "메시지" # 커밋 생성
git log                 # 커밋 기록 확인
```

---

🔹 주요 명령어 정리

명령어	설명
```
git init	Git 저장소 생성
git status	현재 상태 확인
git add .	모든 변경 파일 스테이징
git commit -m "메시지"	스테이징된 변경 커밋
git log	커밋 이력 확인
git diff	변경사항 비교
git reset	커밋 취소 (soft/mixed/hard)
git revert	특정 커밋 되돌리기 (새 커밋 생성)
git rm 파일명	파일 삭제 후 스테이징
git mv A B	파일 이동 or 이름 변경
```




---

🔹 Git 원격(Remote)

명령어	설명
```
git remote add origin URL	원격 저장소 연결
git push (-u) origin master	로컬 master → 원격 업로드   
# -u는 기본값 지정, 없애려면  git branch --set-upstream-to=origin/master
git remote -v 원격 저장소 확인
git pull origin master	원격 master → 로컬 가져오기
git clone URL	원격 저장소 복사
git remote remove origin	원격 저장소 연결 해제
```


*아직 안 배웠지만 브랜치 관련

🔹 Git 브랜치
명령어	설명
```
git branch	브랜치 목록 확인
git branch 브랜치명	브랜치 생성
git checkout 브랜치명	브랜치 전환
git merge 브랜치명	현재 브랜치에 다른 브랜치 병합
git branch -d 브랜치명	브랜치 삭제
git branch --set-upstream-to=origin/master
```
