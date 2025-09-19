# Django Template System & URLs - 동적 웹페이지와 요청/응답

## Template System

### Django Template System이란?
- 데이터를 템플릿과 결합해 동적 웹페이지를 생성하는 도구
- **로직과 표현의 분리**: View(로직) + Template(표현) = 완성된 페이지
- 정적 HTML을 동적 웹페이지로 변환

### Template System의 장점
- **역할 분담**: 개발자(Python 로직) + 디자이너(HTML/CSS)
- **유지보수성**: 로직 변경과 디자인 변경이 독립적
- **재사용성**: 같은 데이터를 다른 디자인으로 표현 가능

## Django Template Language (DTL)

### DTL 주요 문법 4가지

#### 1. Variable (변수) - `{{ }}`
```html
<!-- View에서 전달받은 데이터 출력 -->
<h1>안녕하세요 {{ name }}님!</h1>
<p>나이: {{ age }}세</p>
```

#### 2. Tags (태그) - `{% %}`
```html
<!-- 조건문, 반복문 등 로직 처리 -->

### form 핵심 속성
- **action**: 데이터를 보낼 URL (비어있으면 현재 페이지)
- **method**: HTTP 전송 방식 (GET)
- **name**: 서버에서 데이터를 받을 때 사용할 키 이름

### GET 방식
```html
<form method="GET">
```
- URL에 데이터 표시: `?q=검색어`
- 북마크 가능, URL 공유 가능
- **조회, 검색**에 주로 사용

### View에서 form 데이터 처리 (GET만)
```python
def guestbook(request):
    # GET 요청 (페이지 첫 방문 또는 데이터 전달)
    name = request.GET.get('name')
    message = request.GET.get('message')
    return render(request, 'guestbook.html', context)
```
- HTML 기본 구조의 중복 제거
- 공통 레이아웃 재사용
- 유지보수성 향상

### 상속 관련 DTL 태그

#### `{% extends %}` - 상속받기
```html
{% extends "articles/base.html" %}
```
- 파일 맨 위에 작성 (필수)
- 따옴표 필수 (파일 경로)
- 엔드태그 없음

#### `{% block %}` - 교체 가능한 영역
```html
<!-- 부모 템플릿 (base.html) -->
{% block content %}
    기본 내용
{% endblock %}

<!-- 자식 템플릿 -->
{% block content %}
    새로운 내용으로 교체
{% endblock %}
```
- block 이름 필수 (따옴표 없이)
- 여러 block으로 구역 나누기 가능

### 템플릿 상속 구조 예시
```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}기본 제목{% endblock %}</title>
</head>
<body>
    <header>{% block header %}기본 헤더{% endblock %}</header>
    <main>{% block content %}기본 내용{% endblock %}</main>
    <footer>{% block footer %}기본 푸터{% endblock %}</footer>
</body>
</html>
```

## 요청과 응답

### HTML form을 통한 데이터 전송
- 사용자 입력을 서버로 전송하는 방법
- 로그인, 회원가입, 게시글 작성 등에 사용

### HTML form 기본 구조
```html
<form action="어디로 보낼지" method="어떻게 보낼지">
    <input type="text" name="데이터이름">
    <button type="submit">전송</button>
</form>
```

### form 핵심 속성
- **action**: 데이터를 보낼 URL (비어있으면 현재 페이지)
- **method**: HTTP 전송 방식 (GET/POST)
- **name**: 서버에서 데이터를 받을 때 사용할 키 이름

### GET vs POST 방식

#### GET 방식
```html
<form method="GET">
```
- URL에 데이터 표시: `?q=검색어`
- 북마크 가능, URL 공유 가능
- **조회, 검색**에 주로 사용

#### POST 방식
```html
<form method="POST">
    {% csrf_token %}  <!-- POST에서 필수 -->
```
- URL에 데이터 숨김 (HTTP body에 전송)
- 보안이 중요한 데이터에 사용
- **생성, 수정, 삭제**에 주로 사용
- `{% csrf_token %}` 필수 (보안 기능)

### View에서 form 데이터 처리
```python
def guestbook(request):
    if request.method == 'POST':
        # POST로 전송된 데이터 받기
        name = request.POST.get('name')
        message = request.POST.get('message')
    else:
        # GET 요청 (페이지 첫 방문)
        pass
    return render(request, 'guestbook.html', context)
```

## Django URLs

### Variable Routing
- URL에서 변하는 부분을 변수로 받는 기능
- 동적 URL 처리 가능

#### Variable Routing 문법
```python
# urls.py
path('<타입:변수명>/', views.함수명)

# 주요 타입들
path('<int:pk>/', views.detail)        # 정수
path('<str:name>/', views.profile)     # 문자열
path('<slug:title>/', views.detail)      # 슬러그
```

#### View에서 변수 받기
```python
def profile(request, user_id):
    # user_id 변수 사용
    user = get_user(user_id)
    return render(request, 'profile.html', {'user': user})
```

### App URL 정의
- 메인 프로젝트와 각 앱의 URL 역할 분담
- 앱별 독립적인 URL 관리

#### URL 구조
```python
# 메인 프로젝트 urls.py
urlpatterns = [
    path('articles/', include('articles.urls')),  # articles 앱으로 위임
]

# articles/urls.py  
urlpatterns = [
    path('', views.index),                    # /articles/
    path('profile/<int:user_id>/', views.profile),  # /articles/profile/1/
]
```

## URL 이름 지정

### Naming URL Patterns
- URL에 이름을 붙여 하드코딩 방지
- 유지보수성 향상

#### URL에 이름 붙이기
```python
# urls.py
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
]
```

#### DTL URL 태그 사용
```html
<!-- 변수 없는 URL -->
{% url 'index' %}

<!-- 변수 있는 URL -->
{% url 'profile' 1 %}
{% url 'profile' user_id %}
```

### URL 이름 공간 (Namespace)

#### app_name으로 네임스페이스 분리
```python
# articles/urls.py
app_name = 'articles'  # 네임스페이스 설정

urlpatterns = [
    path('', views.index, name='index'),
]
```

#### 템플릿에서 네임스페이스 사용
```html
<!-- 기존 -->
{% url 'index' %}

<!-- 네임스페이스 사용 -->
{% url 'articles:index' %}
{% url 'accounts:login' %}
```

### 네임스페이스의 장점
- 앱별 URL 이름 충돌 방지
- 어떤 앱의 URL인지 명확
- 프로젝트 확장 시 안전성

## 참고사항

### DTL 주의사항
- Python 코드 직접 실행 불가
- 메서드 호출 시 괄호 없음: `{{ user.get_name }}`
- DTL 문법만 사용 가능

### Trailing Slashes
- Django는 URL 끝에 슬래시(/)를 자동 추가
- URL 패턴에 항상 끝에 `/` 붙이기 권장

### 코드 작성 흐름
**URL → View → Template** 순서로 데이터 흐름에 따라 개발

### 추가 템플릿 경로
```python
# settings.py
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],  # 프로젝트 공통 템플릿
    }
]
```