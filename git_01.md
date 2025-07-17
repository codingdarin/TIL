# Git & GitHub 교안

## 🔰 1. Git 개요

### 🔹 Git이란?

* **분산 버전 관리 시스템 (DVCS: Distributed Version Control System)**
* 코드의 변경 이력(버전)을 관리하고, 협업을 원활하게 해줌

### 🔹 Git을 쓰는 이유

* 이전 버전 복원 가능
* 실수한 코드 복구 가능
* 여러 사람이 동시에 작업 가능
* 충돌 감지 및 병합 도구 제공

### 🔹 Git vs GitHub

* **Git**: 버전 관리 도구 (로컬에서도 사용 가능)
* **GitHub**: Git 저장소를 온라인에서 공유하고 협업할 수 있게 해주는 플랫폼

---

## 🛠️ 2. Git 설치 및 환경 설정

### 🔹 Git 설치

* [https://git-scm.com/downloads](https://git-scm.com/downloads) 에서 설치

### 🔹 Git 설정

```bash
git config --global user.name "사용자이름"
git config --global user.email "이메일주소"
git config --global init.defaultBranch master
```

### 🔹 설정 확인

```bash
git config --list
```

---

## 📁 3. Git 기본 명령어 (2시간)

### 🔸 git init

* Git 저장소 초기화 (로컬에 .git 폴더 생성 -> 타겟팅 역할)

```bash
git init
```

### 🔸 git status

* 현재 브랜치 상태 확인

```bash
git status
```

### 🔸 git add

* 변경된 파일을 스테이징 영역에 추가

```bash
git add 파일명  # 특정 파일
git add .       # 해당 디렉토리(.)의 전체 파일
```

### 🔸 git commit

* 스테이징된 변경 내용을 커밋 (버전 생성)

```bash
git commit -m "커밋 메시지"
```

### 🔸 git log

* 커밋 로그 확인

```bash
git log --oneline  # 간략한 커밋 목록
git log -f         # 파일까지 표시
```

### 🔸 git restore

* 변경 내용 되돌리기

```bash
git restore 파일명         # 워킹 디렉토리 되돌리기
```

---

## 🔗 5. GitHub 원격 저장소 연동 (1시간)

### 🔸 GitHub 저장소 생성

* github.com 접속 > New Repository 클릭

### 🔸 원격 저장소 등록

```bash
git remote add origin https://github.com/계정명/저장소명.git
```

### 🔸 원격 저장소 확인

```bash
git remote -v
```

### 🔸 push (로컬 → GitHub)

* 로컬에서 작업한 내용을 원격 저장소(GitHub)에 업로드하는 명령어
* 주로 로컬 브랜치의 최신 커밋을 GitHub에 반영할 때 사용
* `-u` 옵션은 이후부터 git push만 입력해도 해당 원격 브랜치와 연결되도록 설정

```bash
git push -u origin master  # 최초 1회만 -u 옵션 사용
git push                   # 이후엔 간단히 이렇게만 사용 가능
```

📝 참고: push 전에 로컬 브랜치와 원격 브랜치 이름이 같아야 오류가 적음

### 🔸 pull (GitHub → 로컬)

* 원격 저장소(GitHub)의 변경 사항을 로컬 저장소로 가져오는 명령어
* 다른 사람이 올린 변경 사항을 받아오거나, 여러 디바이스에서 동기화할 때 사용
* 자동으로 `fetch` + `merge` 과정을 수행함

```bash
git pull origin master
```

📝 참고: 충돌(conflict)이 날 수 있으므로, pull 전에 작업 내용을 commit해두는 것이 좋음

### 🔸 clone (복제)

```bash
git clone https://github.com/계정명/저장소명.git
```

---

## 🧹 6. 파일 관리 (30분)

### 🔸 git rm

* 파일 삭제 및 커밋
  
```bash
git rm 파일명
```

### 🔸 git mv

* 파일의 이름 변경과 폴더 이동 모두 가능

Git이 삭제/생성 대신 이동으로 인식하도록 처리함

```bash
git mv 이전경로/이름 새경로/이름  # 이름 변경 또는 디렉토리 이동
```

### 🔸 .gitignore

* Git이 추적하지 않을 파일/폴더 지정

```
__pycache__/
*.log
.env
```

---

## 🧰 8. 원격 저장소 관리 (30분)

### 🔸 원격 저장소 변경

```bash
git remote set-url origin 새주소
```

### 🔸 원격 저장소 제거

```bash
git remote remove origin
```

### 🔸 새 원격 저장소 연결 (폴더 A에서 → B로 변경 시)

```bash
git remote remove origin
# 이후 다시 add
```

---

## ♻️ 9. 리버트와 리셋

### 🔸 git revert

* 기존 커밋을 취소하는 **새로운 커밋**을 생성함 (히스토리 보존)

```bash
git revert 커밋ID
```

* 되돌린다는 의미지만 기록은 남기기 때문에 협업 시 안전함
* 충돌이 발생하면 수동으로 수정 후 다시 커밋 필요

### 🔸 git reset

* 커밋을 되돌림 (로컬 기록에서 이전 상태로 이동)
* 기록을 직접 삭제하므로 협업 중에는 주의해야 함

#### ✅ reset 모드 요약

* `--soft`: 커밋만 되돌리고, 스테이징 상태 유지
* `--mixed`: 커밋과 스테이징을 모두 되돌리고, 작업 디렉토리는 유지 (기본값)
* `--hard`: 커밋, 스테이징, 작업 파일까지 모두 되돌림 (복구 불가)

```bash
# 소프트 리셋: HEAD만 이동하고 파일 내용은 그대로
git reset --soft HEAD~1

# 믹스드 리셋: HEAD와 인덱스 되돌림, 워킹 디렉토리는 유지
git reset --mixed HEAD~1

# 하드 리셋: 모두 되돌림 (주의)
git reset --hard HEAD~1
```

📝 차이 요약:

* `reset`: 기록 자체를 지움 → **단독 작업용**
* `revert`: 기록 보존하며 취소 → **협업 시 안전**

---

## ✅ 10. 실습 프로젝트 예시

* "Hello Git" 프로젝트를 만들고
* 브랜치 나눠서 수정 및 병합 실습
* GitHub에 업로드하고 동료와 코드 공유 및 리뷰

