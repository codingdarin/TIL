# Django Authentication System
# Django Cookie & Session

## HTTP (HyperText Transfer Protocol)

### HTTP란?
- HTML 문서 같은 리소스를 가져올 수 있도록 해주는 규약
- 웹에서의 모든 데이터 교환의 기초
- 웹 브라우저와 서버가 서로 대화하기 위해 사용하는 공통 언어 또는 약속

### HTTP의 동작 방식
- 브라우저가 서버에 요청(Request)을 보냄
- 서버는 HTML 파일 등을 응답(Response)으로 보냄
- 응답 후 연결이 끊김

---

## HTTP의 특징

### 1. 비연결 지향 (Connectionless-oriented)
- 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
- 클라이언트는 서버와 서로 연결되어 있는 상태가 아님
- **목적**: 서버가 문서를 다 읽을 때까지 모든 사용자가 연결을 유지하면 서버 메모리 자원을 많이 차지하게 됨. 이러한 자원 낭비를 막기 위해 비연결 방식을 채택함

### 2. 무상태 (Stateless)
- 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
- **무상태의 의미**:
  - 장바구니에 담은 상품을 유지할 수 없음
  - 로그인 상태를 유지할 수 없음

### HTTP가 무상태로 설계된 이유
- 서버가 모든 클라이언트 상태를 기억하면 자원 관리가 매우 복잡해짐
- 클라이언트가 다른 서버에 연결되어도 상태 응답이 가능하여 확장성이 좋음
- 서버 부담을 줄이고 대규모 웹 서비스 구축에 유리함

### 비연결과 무상태의 관계
- 비연결 지향이기 때문에 무상태가 됨
- 연결이 끊기면 이전 요청을 기억할 수 없음
- 이 문제를 해결하기 위해 쿠키와 세션이 필요함

---

## 쿠키 (Cookie)

### 쿠키란?
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 웹사이트가 사용자의 브라우저에 남기는 작은 데이터 조각
- HTTP 무상태 문제를 해결하여 상태를 유지할 수 있게 함

### 쿠키의 특징
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식
- key-value 형식의 데이터
- 브라우저가 자동으로 서버에 전송함

### 쿠키 동작 과정
1. 브라우저가 웹 서버에 웹 페이지를 요청
2. 웹 서버는 요청된 페이지와 함께 쿠키를 포함한 응답을 브라우저에게 전송
3. 브라우저는 받은 쿠키를 저장소에 저장하고, 쿠키의 속성(만료 시간, 도메인, 주소 등)도 함께 저장
4. 이후 브라우저가 같은 웹 서버에 웹 페이지를 요청할 때, 저장된 쿠키 중 해당 요청에 적용 가능한 쿠키를 포함하여 함께 전송
5. 웹 서버는 받은 쿠키 정보를 확인하고, 필요에 따라 사용자 식별, 세션 관리 등을 수행
6. 웹 서버는 요청에 대한 응답을 보내며, 필요한 경우 새로운 쿠키를 설정하거나 기존 쿠키를 수정할 수 있음

### 쿠키 저장 및 전송 방식
- **저장 방식**: 브라우저(클라이언트)는 쿠키를 KEY-VALUE의 데이터 형식으로 저장
- **추가 속성**: 쿠키에는 이름, 값 외에도 만료 시간, 도메인, 경로 등의 추가 속성이 포함됨
- **전송 과정**:
  - 서버는 HTTP 응답 헤더의 `Set-Cookie` 필드를 통해 클라이언트에게 쿠키를 전송
  - 브라우저는 받은 쿠키를 저장해 두었다가, 동일한 서버에 재요청 시 HTTP 요청 Header의 `Cookie` 필드에 저장된 쿠키를 함께 전송

### 쿠키 사용 목적

#### 1. 세션 관리 (Session management)
- 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리

#### 2. 개인화 (Personalization)
- 사용자 선호 설정(언어 설정, 테마 등) 저장

#### 3. 추적, 수집 (Tracking)
- 사용자 행동을 기록 및 분석

### 쿠키의 주요 용도
- 두 요청이 동일한 브라우저에서 들어왔는지 판단할 때 주로 사용
- 사용자의 로그인 상태를 유지
- 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억시키는 역할
- **서버에게 "나 로그인 된(인증된) 사용자야!" 라는 인증 정보가 담긴 쿠키를 매 요청마다 계속 보냄**

### 쿠키 사용 시 주의사항
- 쿠키는 탈취될 수 있으므로 비밀번호 등 민감한 정보는 절대 직접 저장하면 안 됨
- 쿠키는 모든 요청에 포함되어 전송되므로, 크기를 최소화해야 사이트 성능에 유리함

---

## 세션 (Session)

### 세션이 필요한 이유
- 쿠키는 브라우저에 저장되어 사용자가 볼 수 있고 조작 가능함
- 악의적인 사용자가 쿠키를 탈취하거나 수정할 수 있음
- 민감한 정보를 쿠키에 직접 담으면 보안 위험이 큼

### 세션의 해결 방법
- 중요한 정보는 서버에 저장 (세션)
- 브라우저에는 세션 ID만 쿠키로 저장

### 세션 동작 방식
1. **로그인 성공**: 서버가 세션을 생성하고 세션에 사용자 정보 저장
   - 예: `세션 abc123 = {user_id: 1, username: 'hong'}`
2. **세션 ID를 쿠키로 전송**: 서버가 `Set-Cookie: sessionid=abc123`을 브라우저에 보냄
3. **다음 요청**: 브라우저가 자동으로 `Cookie: sessionid=abc123`을 보냄
4. **서버 확인**: 서버가 세션 ID로 세션 데이터를 찾아 사용자 식별

### 쿠키 vs 세션 비교

| 구분 | 쿠키 | 세션 |
|-----|------|------|
| 저장 위치 | 브라우저 | 서버 |
| 보안 | 탈취/조작 위험 | 상대적으로 안전 |
| 저장 데이터 | 모든 데이터 | 세션 ID만 |

### 세션이 더 안전한 이유

#### 쿠키만 사용하는 경우
```
Set-Cookie: user_id=1
Set-Cookie: username=hong
```
- 브라우저 개발자 도구로 쿠키 값 확인 가능
- `user_id=1`을 `user_id=999`로 직접 수정 가능
- 서버는 쿠키 값을 그대로 믿음 → 다른 사용자로 로그인됨

#### 세션 사용하는 경우
```
서버 세션 저장소:
  sessionid_abc123 = {user_id: 1, username: 'hong'}

브라우저 쿠키:
  sessionid=abc123
```
- 브라우저에는 세션 ID만 보임
- 세션 ID를 수정해도 서버에 해당 세션이 없으면 무효
- 세션 ID는 예측 불가능한 긴 랜덤 문자열

### 세션의 보안 강화

#### 탈취 방지
- HTTPS 사용: 네트워크 암호화로 중간 가로채기 방어
- HttpOnly 쿠키: JavaScript로 쿠키 접근 불가 (XSS 공격 방어)
- Secure 쿠키: HTTPS에서만 전송

#### 탈취 시 피해 최소화
- 세션 만료 시간 설정: 30분 후 자동 로그아웃
- IP 체크: 로그인한 IP와 다른 IP에서 접속 시 재인증
- 의심 활동 감지 시 서버에서 세션 강제 삭제

### 세션 하이재킹 (Session Hijacking)
- 세션 ID를 탈취하여 다른 사용자로 로그인하는 공격
- 세션 ID도 탈취 가능하지만, 쿠키에 직접 저장하는 것보다 훨씬 안전함
- 여러 보안 장치를 통해 탈취를 어렵게 만들고 피해를 최소화함

---

## 자동 로그인

### 일반 로그인 vs 자동 로그인

| 구분 | 일반 로그인 | 자동 로그인 |
|-----|------------|------------|
| 저장 방식 | 세션 ID (단기) | 장기 토큰 |
| 만료 시간 | 짧음 (30분) | 김 (30일) |
| 브라우저 닫으면 | 로그아웃됨 | 유지됨 |
| 보안 | 더 안전 | 덜 안전 (편의성↑) |

### 자동 로그인 동작 방식
1. 자동로그인 체크 시: `Set-Cookie: auto_login_token=xyz789; Max-Age=2592000` (30일)
2. 다음 접속 시: 브라우저가 토큰 전송 → 서버가 토큰 확인 → 자동 로그인 → 새 세션 생성
3. 보안 강화:
   - 중요한 작업(비밀번호 변경, 결제)은 재인증 요구
   - 기기별로 다른 토큰 발급
   - 의심 활동 감지 시 토큰 무효화

### 자동 로그인 주의사항
- 공용 PC에서는 보안 위험이 있음
- 장기 토큰이 남아있어 다른 사람이 접속할 수 있음

---

## 정리

### HTTP의 문제와 해결
- HTTP는 비연결 지향, 무상태 특성으로 상태를 유지할 수 없음
- 쿠키와 세션을 통해 상태 유지 문제를 해결함

### 쿠키와 세션의 관계
- 쿠키는 브라우저에 데이터를 저장
- 세션은 서버에 데이터를 저장하고 브라우저에는 ID만 저장
- 둘을 함께 사용하여 안전하게 상태를 유지함

### 보안 원칙
- 민감한 정보는 절대 쿠키에 직접 저장하지 않음
- 세션을 사용하여 서버가 데이터를 관리함
- HTTPS, HttpOnly, Secure 등의 보안 장치를 함께 사용함

---

# Django Authentication System

## Django 인증 시스템

### 인증 시스템 개요
- Django에서 사용자 인증과 관련된 기능을 모아 놓은 시스템
- 인증에 중요한 기본적인 기능을 제공

### 제공 기능
1. **User Model**: 사용자 인증 후 연결될 User Model 관리
2. **Session 관리**: 로그인 상태를 유지하고 서버에 저장하는 방식 관리
3. **기본 인증(Id/Password)**: 로그인/로그아웃 등 다양한 기능 제공

---

## Custom User Model

### Custom User Model이 필요한 이유
- Django 기본 User Model은 username, email, password 등 기본 필드만 제공
- 프로필 이미지, 전화번호, 생년월일 등 추가 정보를 저장하려면 커스텀 필요
- 나중에 필드를 추가하기가 매우 복잡하므로 프로젝트 시작 시 무조건 생성

### Custom User Model 생성 순서

#### 1. accounts 앱 생성 및 등록
```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = []
```

```python
# crud/urls.py
urlpatterns = [
    ...,
    path('accounts/', include('accounts.urls')),
]
```

#### 2. AbstractUser 상속받아 User 모델 생성
```python
# accounts/models.py
from django.contrib.auth.models import import AbstractUser

class User(AbstractUser):
    pass
```

- AbstractUser 클래스를 상속받는 커스텀 User 클래스 작성
- 기존 User 클래스도 AbstractUser를 상속받기 때문에 완전히 같은 모습을 가짐

#### 3. settings.py에서 AUTH_USER_MODEL 설정
```python
# settings.py
AUTH_USER_MODEL = 'accounts.User'
```

- Django 프로젝트에서 사용하는 기본 User 모델을 커스텀 User 모델로 변경
- 수정 전 기본 값은 'auth.User'

#### 4. admin.py에 User 모델 등록
```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

- 기본 User 모델이 아니므로 등록하지 않으면 admin 페이지에 출력되지 않음

### Custom User Model 주의사항
- **프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 반드시 완료해야 함**
- User 테이블은 다른 많은 테이블과 외래키로 연결되므로 나중에 변경이 매우 복잡함
- 이미 migrate를 했다면 DB를 삭제하고 처음부터 다시 시작해야 함
- Django 공식 문서에서도 프로젝트 시작 시 Custom User Model 생성을 강력히 권장

### 실무 프로젝트 시작 순서
1. 프로젝트 생성
2. accounts 앱 생성
3. Custom User 모델 작성 (AbstractUser 상속)
4. settings.py에 AUTH_USER_MODEL 설정
5. makemigrations, migrate 실행
6. 다른 앱들 개발 시작

---

## Login

### 로그인이란?
- 클라이언트와 서버 간의 상태 정보를 유지하기 위해 쿠키와 세션을 사용
- 서버에 "나"임을 인증하는 과정
- **인증(id/password)을 완료하고, Session을 만들고 클라이언트와 연결하는 것**

### 로그인 과정
1. **로그인(id/password)**: 사용자가 아이디와 비밀번호 입력
2. **로그인 인증**: 서버가 아이디/비밀번호 확인
3. **세션 생성 후 서버 저장**: 인증 성공 시 서버에 세션 생성
4. **클라이언트에 쿠키 전달**: 서버가 세션 ID를 쿠키로 클라이언트에게 전송

### CRUD 관점에서의 로그인
- **User 데이터 관점**: Read (User 조회)
- **Session 데이터 관점**: Create (세션 생성)
- 로그인 = Read User + Create Session

---

## Django 로그인 구현

### 1. AuthenticationForm
- Django가 제공하는 로그인 전용 폼
- 사용자 인증(id/password 확인)을 위한 폼
- 일반 ModelForm과 다르게 `request`를 첫 번째 인자로 받음
- username과 password 필드를 가지고 있음

### 2. login() 함수
```python
from django.contrib.auth import login
```
- Django가 제공하는 로그인 함수
- 인증된 사용자를 로그인 시키는 함수
- 세션을 생성하는 역할
- `login(request, user)` 형태로 사용

#### 매개변수
- **request**: 현재 사용자의 세션 정보에 접근하기 위해 사용
- **user**: 어떤 사용자가 로그인 되었는지를 기록하기 위해 사용

### 3. get_user() 메서드
- AuthenticationForm의 인스턴스 메서드
- 유효성 검사를 통과했을 경우, 로그인 한 사용자 객체를 반환
- `is_valid()` 통과 후에만 사용 가능

---

## 로그인 구현 코드

### URL 설정
```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]
```

### View 작성
```python
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)
```

**주의사항:**
- `login` 함수 이름과 Django의 `login()` 함수가 겹치므로 `as auth_login`으로 이름 변경
- `AuthenticationForm`은 `request`를 첫 번째 인자로 받음 (일반 Form과 다름)
- `form.get_user()`: 인증된 사용자 객체 반환

### Template 작성
```html
<!-- accounts/login.html -->
<h1>로그인</h1>
<form action="{% url 'accounts:login' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button>로그인</button>
</form>
```

### 로그인 동작 흐름
1. GET 요청: 빈 로그인 폼 보여줌
2. 사용자 입력: id/password 입력 후 제출
3. POST 요청:
   - AuthenticationForm으로 데이터 검증
   - is_valid(): DB에서 User 조회 + 비밀번호 확인
   - 성공 시: form.get_user()로 User 객체 가져옴
4. login() 함수 호출: 세션 생성
5. 리다이렉트: 메인 페이지로 이동

---

## Template with Authentication data

### request.user
- Django는 템플릿에서 자동으로 `user` 변수를 제공
- 브라우저가 요청할 때 세션 ID 쿠키를 함께 보냄
- Django가 세션 ID로 세션 데이터 조회
- 세션에 저장된 User 정보를 `request.user`에 자동 할당

### user 객체 속성

**user.is_authenticated**
- 로그인 되어있으면 `True`
- 로그인 안 되어있으면 `False`
- 가장 많이 사용하는 속성

**user.username**
- 로그인한 사용자의 username

**user.is_anonymous**
- 로그인 안 된 익명 사용자면 `True`
- `is_authenticated`의 반대

### 템플릿 사용 예시
```html
<!-- base.html -->
<body>
  <h1>Hello, {{ user.username }}!</h1>
  
  {% if user.is_authenticated %}
    <p>로그인 되어있습니다.</p>
    <a href="{% url 'accounts:logout' %}">로그아웃</a>
  {% else %}
    <p>로그인이 필요합니다.</p>
    <a href="{% url 'accounts:login' %}">로그인</a>
  {% endif %}
</body>
```

### 로그인하지 않은 경우
- `user`는 `AnonymousUser` 객체
- `user.is_authenticated` = False
- `user.username` = 빈 문자열