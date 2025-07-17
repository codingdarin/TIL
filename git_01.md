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

```bash
git push -u origin master  # 최초 1회
```

### 🔸 pull (GitHub → 로컬)

```bash
git pull origin master
```

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

* 파일 이름 변경

```bash
git mv 기존이름 새이름
```

### 🔸 .gitignore

* Git이 추적하지 않을 파일/폴더 지정


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
