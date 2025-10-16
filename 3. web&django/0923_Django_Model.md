# Django Model 및 Migrations

## Model

### Model이란?
- 데이터베이스와 Python 클래스(객체)로 추상화된 형태로 상호작용
- Django의 강력한 기능: 개발자가 데이터베이스에 대한 깊은 지식 없이도 쉽게 데이터 관리 가능
- 유지보수 및 확장성 측면: 데이터베이스 변경 시에도 코드 수정 최소화, 재사용 가능한 데이터 모델 사용 가능

### Model을 통한 DB 관리
- **urls.py**: 사용자 요청의 시작점
- **views.py**: 요청을 처리하고 models.py를 통해 데이터를 다룸
- **models.py**: 데이터베이스와 상호작용
- **templates**: views.py로부터 받은 데이터를 사용자에게 보여줌

## Model class

### Model class란?
- 데이터베이스 테이블의 구조를 설계하는 '청사진(blueprint)' 역할
- 어떤 데이터(컬럼)를 저장할지, 그 데이터의 형태(타입, 길이 등)를 Python 코드로 정의

### Model 클래스 작성 예시

```python
# articles/models.py
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

- `models.Model` 상속 필수 (django.db.models 모듈의 Model 클래스)
- 클래스 변수 = 테이블 컬럼
- id 필드는 Django가 자동 생성
- 작성한 모델 클래스는 최종적으로 DB에 다음과 같은 테이블 구조를 만듦

| id | title | content |
|----|-------|---------|
| .. | ..    | ..      |

## Model Field

### Model Field란?
- DB 테이블의 필드(열), 즉 데이터 타입과 제약 조건을 정의
- Django는 다양한 필드 정의를 제공하여 DB 컬럼을 자동 생성하고 데이터 입력 시 유효성 검사 자동 수행
- 적절한 필드 정의는 애플리케이션의 안정성 향상

### Field types (필드 유형)
데이터베이스에 저장될 "데이터의 종류"를 정의

**문자열 필드**
- `CharField`: 제한된 길이의 문자열 저장 (max_length 필수)
- `TextField`: 길이 제한 없는 대용량 텍스트 저장

**숫자 필드**
- `IntegerField`: 정수
- `FloatField`: 실수

**날짜/시간 필드**
- `DateField`: 날짜
- `TimeField`: 시간
- `DateTimeField`: 날짜와 시간

**파일 관련 필드**
- `FileField`: 파일
- `ImageField`: 이미지

### Field options (필드 옵션)
필드의 "동작"과 "제약 조건"을 정의

**제약 조건(Constraint)**
- 특정 규칙을 강제하기 위해 데이터의 열이나 행에 적용되는 규칙이나 제한사항
- 예: 숫자만 저장되도록 제한, 문자가 100자까지만 저장되도록 제한

**주요 필드 옵션**
- `null`: DB에서 NULL 값을 허용할지 여부 결정 (기본값: False)
- `blank`: form에서 빈 값을 허용할지 여부 결정 (기본값: False)
- `default`: 필드의 기본값 설정

**DateTimeField 전용 옵션**
- `auto_now`: 데이터가 저장될 때마다 자동으로 현재 날짜시간 저장
- `auto_now_add`: 데이터가 처음 생성될 때만 자동으로 현재 날짜시간 저장

## Migrations

### Migrations란?
- model 클래스의 변경사항(필드 생성, 수정, 삭제 등)을 DB에 최종 반영하는 방법
- 모든 변경 사항이 코드로 관리되어 협업 시 모델 변경 내역에 대한 추적과 공유가 수월

### Migrations 과정

```
model class (설계도 초안)
    ↓ makemigrations
migration 파일 (최종 설계도)
    ↓ migrate
db.sqlite3 (DB)
```

### 1단계: makemigrations

```bash
$ python manage.py makemigrations
```

- 역할: model class를 기반으로 최종 설계도(migration)를 작성
- 결과: `articles/migrations/0001_initial.py` 파일 생성
- 모델 변경을 감지하고 migration 파일을 생성하는 명령어

### 2단계: migrate

```bash
$ python manage.py migrate
```

- 역할: 최종 설계도를 DB에 전달하여 반영
- 마이그레이션 파일의 Python 코드를 SQL 문으로 자동 변환하여 DB에 실행
- 변환 과정: Python 코드 → 번역 → SQL 쿼리로 → 데이터베이스 실행

### 언제 Migration이 필요한가?

**model class에 변경사항(1)이 생겼다면, 반드시 새로운 설계도를 생성(2)하고, 이를 DB에 반영(3)해야 한다.**

(1) model class 생성/수정 → (2) makemigrations → (3) migrate

### 이미 생성된 테이블에 필드 추가하기

기존 데이터가 있는 테이블에 새 필드 추가 시 기본값 설정 필요

```python
# articles/models.py
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

makemigrations 실행 시 기본값 설정 프롬프트 표시:
- 1번: 현재 대화에서 유지하면서 직접 기본 값 입력 (일회성 기본값, 기존 데이터에만 적용)
- 2번: 현재 대화에서 나간 뒤 models.py에 기본 값 관련 설정

날짜 데이터는 Django가 제안하는 기본값(timezone.now) 사용 권장 (enter로 선택)

### Migration 파일 관리 주의사항
- 마이그레이션 파일은 되도록이면 직접 건드리지 않음
- migrations 폴더 내 자동으로 생성된 파일들은 직접 수정하거나 삭제하지 않는 것이 원칙
- Django는 설계도를 쌓아가면서 추후 문제 발생 시 복구하거나 되돌릴 수 있도록 함 (git commit과 유사)

## Admin site

### 관리자 인터페이스란?
- Django가 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스
- 주요 기능: 데이터베이스 모델의 CRUD(생성, 읽기, 업데이트, 삭제) 작업을 간편하게 수행
- 활용: 빠른 프로토타이핑, 비개발자 데이터 관리, 내부 시스템 구축에 이상적

### Django admin 계정 생성

**1. 터미널 열기**
- Django 프로젝트 폴더로 이동 (manage.py 파일이 있는 위치)

**2. 관리자 계정 생성 명령어 입력**

```bash
$ python manage.py createsuperuser
```

**3. 정보 입력**
- 사용자 이름(username): 관리자 페이지 로그인 아이디
- 이메일(email address): 선택 사항 (엔터로 넘어가도 됨)
- 비밀번호(password): 로그인 비밀번호 (입력 시 콘솔 창에 표시 안 됨)
- 비밀번호 확인(password(again)): 비밀번호 재입력

### Admin site 접속

**웹 브라우저에서 주소 입력**
- http://127.0.0.1:8000/admin
- 생성한 관리자 계정으로 로그인

### Admin site에 모델 클래스 등록

admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능

```python
# articles/admin.py
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

등록 후 Admin 페이지에서 ARTICLES 섹션이 생기고 Articles 모델에 대한 CRUD 작업 가능

### Admin site에서 데이터 관리
- Articles 앱에서 article에 대한 CRUD(생성, 읽기, 업데이트, 삭제) 수행 가능
- + Add 버튼: 새로운 데이터 생성
- Change 버튼: 기존 데이터 수정
- Delete 버튼: 데이터 삭제
- 상세 페이지에서 데이터 수정 및 삭제 가능

## 참고

### 데이터베이스 초기화 방법

**1. Migration 파일 삭제**
- makemigrations 명령어로 생성되는 설계도(Migration 파일) 삭제
- 단, `__init__.py`와 `migrations` 폴더 자체는 삭제 금지

**2. db.sqlite3 파일 삭제**

### Migrations 기타 명령어

**showmigrations**

```bash
$ python manage.py showmigrations
```

- migrations 파일들이 migrate 됐는지 안 됐는지 여부를 확인
- [X] 표시: migrate 완료

**sqlmigrate**

```bash
$ python manage.py sqlmigrate articles 0001
```

- 해당 migrations 파일이 SQL 언어로 어떻게 번역되어 DB에 전달되는지 확인
- 형식: `python manage.py sqlmigrate <앱 이름> <마이그레이션 이름>`

### 최초 migrate 시 출력 내용이 많은 이유
- Django 프로젝트가 동작하기 위해 미리 작성되어 있는 기본 내장 app들에 대한 migration 파일들을 함께 migrate하기 때문
- INSTALLED_APPS에 등록된 모든 앱(admin, auth, contenttypes, sessions, messages, staticfiles 등)의 migration이 함께 실행됨

### SQLite

**SQLite란?**
- 데이터베이스 관리 시스템 중 하나이며 Django의 기본 데이터베이스로 사용됨

**특징**
- 파일 기반: 데이터베이스가 하나의 파일로 저장되어 설치/설정 없이 간편하게 복사/이동/백업 가능
- 가볍고 빠름: 별도 서버 없이 파일로 직접 데이터 처리, 소규모 앱이나 모바일 환경에 최적화
- 높은 호환성: 다양한 운영체제와 프로그래밍 언어에서 폭넓게 사용 가능

**주의사항**
- db.sqlite3 파일은 Git 등 버전 관리 시스템에서 관리하지 않는 것이 원칙
- 데이터가 변경될 때마다 파일 전체가 변경됨
- SQLite 파일은 로컬 컴퓨터에 저장된 데이터 기록
- .gitignore 파일에 db.sqlite3를 추가하여 Git 버전 관리에서 제외해야 함

**gitignore.io**
- 개발자들이 .gitignore 파일을 쉽게 생성할 수 있도록 도와주는 웹 서비스
- Django를 키워드로 추가하면 db.sqlite3가 자동으로 포함된 .gitignore 파일 생성