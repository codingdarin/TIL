# 웹 개발 기초 - Web Application & Framework & 가상환경

## Web Application

### 클라이언트와 서버
- **클라이언트(Frontend)**: 사용자가 직접 보고 조작하는 부분 (웹 브라우저 화면)
- **서버(Backend)**: 데이터를 처리하고 저장하는 부분 (사용자 눈에 보이지 않음)

### 동작 원리 (Request & Response)
1. 클라이언트가 요청(Request) 전송
2. 서버가 요청을 처리하고 응답(Response) 전송  
3. 브라우저가 응답을 받아 화면에 표시

### Frontend vs Backend 역할
- **Frontend**: HTML(구조), CSS(디자인), JavaScript(동적 기능)
- **Backend**: 데이터베이스 처리, 사용자 인증, 비즈니스 로직

## Framework

### Framework란?
- 미리 만들어진 개발 도구 세트
- 자주 사용되는 기능들을 미리 구현해둔 코드 집합

### Web Framework의 장점
- 개발 시간 단축
- 검증된 코드 사용으로 버그 감소
- 일정한 코딩 규칙 제공
- 보안, 라우팅, 데이터베이스 연결 등 기본 기능 제공

### Django Framework 특징
- Python 기반 웹 프레임워크
- "배터리 포함" 철학: 웹 개발 필요 기능 대부분 기본 제공
- 관리자 페이지 자동 생성
- 강력한 보안 기능
- Instagram, YouTube, Dropbox 등에서 사용

## 가상 환경 (Virtual Environment)

### 가상 환경의 목적
- **독립된 Python 작업 공간** 생성
- 프로젝트별로 다른 패키지 버전 사용 가능
- 패키지 충돌 방지
- 프로젝트 의존성 관리

### 가상 환경이 필요한 이유
- 프로젝트 A: Django 3.2 필요
- 프로젝트 B: Django 4.1 필요
- 전역 환경에서는 하나의 버전만 설치 가능 → 충돌 발생

### 가상 환경 생성 및 관리
```python
# 가상 환경 생성 (관례적으로 venv 이름 사용)
python -m venv venv

# 활성화 (Windows)
venv\Scripts\activate

# 활성화 (Mac/Linux)
source venv/bin/activate

# 활성화 확인: 명령 프롬프트 앞에 (venv) 표시

# 종료
deactivate
```

### 가상 환경 사용 흐름
1. **생성** (처음 한 번만)
2. **활성화** (작업할 때마다)
3. **개발 작업** (패키지 설치, 코딩 등)
4. **종료** (작업 완료 후)

## 의존성 패키지 (Dependency Packages)

### 의존성 패키지란?
- 내 프로젝트가 실행되기 위해 **반드시 필요한** 외부 라이브러리
- 내가 `import`해서 사용하는 패키지들
- 프로젝트 기준으로 "필수적인" 패키지

### 의존성 패키지 관리
```python
# 패키지 설치
pip install django

# 현재 설치된 패키지 확인
pip list        # 사람이 보기 편한 형태
pip freeze      # requirements.txt 형태

# 의존성 목록 저장
pip freeze > requirements.txt

# 저장된 의존성으로 일괄 설치
pip install -r requirements.txt
```

### pip list vs pip freeze
- **pip list**: 테이블 형태, 사람이 읽기 편함
- **pip freeze**: `패키지==버전` 형태, 설치 명령어와 동일한 형식
- **requirements.txt**: pip freeze 결과를 저장, 다른 환경에서 동일한 패키지 설치 가능

### 글로벌 환경 vs 가상 환경
- **글로벌 환경**: 시스템 전체에 패키지 설치, 모든 프로젝트에서 공유
- **가상 환경**: 프로젝트별 독립된 패키지 환경, 충돌 방지

## 협업을 위한 프로젝트 설정

### 협업에 필요한 필수 파일들

#### 1. requirements.txt
- 프로젝트의 의존성 패키지 목록
- 팀원들이 동일한 환경을 구축할 수 있도록 함
```python
Django==4.2.7
Pillow==9.5.0
requests==2.28.2
```

#### 2. README.md  
- 프로젝트 설정 및 실행 방법 안내
- 새로운 팀원이 프로젝트를 시작할 수 있도록 가이드 제공
```markdown
# 프로젝트 설정 방법
1. 가상환경 생성: python -m venv venv
2. 가상환경 활성화: venv\Scripts\activate  
3. 패키지 설치: pip install -r requirements.txt
4. 서버 실행: python manage.py runserver
```

#### 3. .gitignore
- Git에 올리지 않을 파일/폴더 목록
- 가상환경, 캐시 파일 등 개인 환경 파일 제외
```
venv/
__pycache__/
*.pyc
db.sqlite3
```

### 협업 시나리오
1. **팀원 A**: 개발 완료 후 requirements.txt, README.md 작성
2. **팀원 B**: Git에서 코드 다운로드
3. **팀원 B**: README.md 참고하여 환경 설정
4. **팀원 B**: requirements.txt로 동일한 패키지 환경 구축
5. **즉시 개발 시작 가능**

### 문서화의 중요성
- 패키지 버전 불일치 방지
- 설정 방법 통일
- 새로운 팀원의 빠른 온보딩
- 개발 환경 표준화

## Django 프로젝트 생성 및 서버 실행

### Django 설치 및 프로젝트 생성
```python
# 가상환경에서 Django 설치
pip install django

# 프로젝트 생성 (현재 폴더에)
django-admin startproject firstpjt .

# 서버 실행
python manage.py runserver
```

### 프로젝트 구조
```
현재폴더/
├── manage.py          # Django 관리 명령어 실행 파일
├── firstpjt/          # 프로젝트 설정 폴더
│   ├── __init__.py    # Python 패키지 표시 파일
│   ├── settings.py    # 프로젝트 설정 파일
│   ├── urls.py        # URL 라우팅 설정
│   ├── wsgi.py        # 배포용 파일
│   └── asgi.py        # 비동기 배포용 파일
└── venv/              # 가상환경
```

### 점(.) 사용의 장점
- 폴더 중복 방지 (firstpjt/firstpjt/ 구조 방지)
- 깔끔한 프로젝트 구조
- 실무에서 선호하는 방식

## Django Design Pattern (MTV)

### MVC vs MTV 패턴
- **MVC**: Model-View-Controller (일반적인 웹 패턴)
- **MTV**: Model-Template-View (Django의 패턴)

### MTV 구성 요소
- **Model**: 데이터 처리 (데이터베이스 관련)
- **Template**: 사용자 화면 (HTML 파일)
- **View**: 비즈니스 로직 처리 (Python 함수/클래스)

### MTV 동작 흐름
1. 사용자가 URL로 요청
2. View가 요청을 받아 로직 처리
3. Model에서 필요한 데이터 조회
4. Template과 데이터를 결합
5. 완성된 HTML을 사용자에게 응답

## Django 프로젝트와 앱

### 프로젝트 vs 앱 개념
- **프로젝트**: 전체 웹사이트 (예: 인스타그램 전체)
- **앱**: 특정 기능 모듈 (예: 사용자 관리, 게시글, 댓글)

### 앱의 장점
- 기능별 코드 분리로 관리 용이
- 다른 프로젝트에서 재사용 가능
- 팀 개발 시 역할 분담 가능

### 앱 생성 및 등록 (필수 순서)
```python
# 1단계: 앱 생성 (manage.py가 있는 폴더에서)
python manage.py startapp articles

# 2단계: settings.py에 앱 등록
INSTALLED_APPS = [
    'articles',              # 사용자 정의 앱 (위에 추가)
    'django.contrib.admin',
    'django.contrib.auth',
    # ... 기타 Django 기본 앱들
]
```

### 앱 구조
```
articles/
├── migrations/        # 데이터베이스 변경사항
├── __init__.py       
├── admin.py          # 관리자 페이지 설정
├── apps.py           # 앱 설정
├── models.py         # Model (데이터 구조)
├── tests.py          # 테스트 코드
└── views.py          # View (비즈니스 로직)
```

## 요청과 응답

### HTTP Request & Response
- 브라우저에서 URL 입력 = 클라이언트가 서버에 요청(Request)
- Django 서버가 HTML 응답(Response) 전송
- 브라우저가 받은 HTML을 화면에 표시

### 개발 서버 특징
- 자동 재시작: 코드 수정 시 서버 자동 재시작
- 개발 전용: 실제 배포용 아님 (성능, 보안 한계)
- 종료: Ctrl + C

## 코드 작성 흐름

### 데이터 흐름에 따른 개발 순서
**URL → View → Template** 순서로 코드 작성

1. **URL**: 어떤 주소로 요청을 받을지 정의
2. **View**: 요청을 어떻게 처리할지 로직 작성  
3. **Template**: 최종적으로 사용자에게 보여줄 화면 작성

### Template 폴더 구조
```
articles/
└── templates/
    └── articles/
        └── index.html    # 앱이름/템플릿이름 구조로 충돌 방지
```