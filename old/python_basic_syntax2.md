
# Python 자료구조 TIL

## List (리스트)

### 정의
- 1.**여러 개의 값**을 2.**순서대로** 저장하는 3.**변경 가능한** 시퀀스 자료형
- 대괄호 `[]`로 표현

### 특징
- 모든 종류의 데이터 저장 가능 (숫자, 문자열, 리스트, 딕셔너리 등) 
  다른 리스트를 값으로 가진 리스트: '중첩 리스트'
- 인덱싱, 슬라이싱, 길이 확인, 반복 등 **시퀀스 공통 기능** 사용 가능
- 변경 가능하므로 추가, 삭제, 수정 가능

### 예시
```python
# 리스트 생성
empty_list = []
my_list = [1, 2, 3, 'python', ['hello', 'world', '!!!']]

# 인덱싱
print(my_list[0])     # 1
print(my_list[-1])    # ['hello', 'world', '!!!']

# **중첩 리스트 접근**
print(my_list[4][0])   # 'hello'
print(my_list[4][-1])  # '!!!'
# [4]: 리스트 형태의 객체 인덱싱, 
# [0]: 리스트 요소 0번째 인덱싱  

# 슬라이싱
print(my_list[1:3])    # [2, 3]
print(my_list[:2])     # [1, 2]

# 리스트 수정
my_list[0] = 100       
# [100, 2, 3, 'python', ['hello', 'world', '!!!']]
my_list.append(5)      # (끝에 추가)
my_list.insert(1, 'new')  # (특정 위치에 삽입)
```


## Tuple (튜플)

### 정의
- **변경 불가능한** 시퀀스 자료형
- 소괄호 `()`로 표현 (생략 가능)

### 특징
- 한번 생성되면 수정, 추가, 삭제 불가능
- 인덱싱, 슬라이싱, 길이 확인, 반복 등 시퀀스 공통 기능 사용 가능
- 안전성과 무결성 보장으로 파이썬 내부 동작과 안전한 데이터 전달에 주로 사용

### 예시
```python
# 튜플 생성
my_tuple = (1, 2, 3, 'python')
simple_tuple = 1, 2, 3  # 소괄호 생략 가능
single_tuple = (1,)     # 단일 요소 튜플은 쉼표 필요

# 인덱싱
print(my_tuple[0])      # 1
print(my_tuple[-1])     # 'python'

# 슬라이싱
print(my_tuple[1:3])    # (2, 3)

# 튜플 언패킹
x, y = 10, 20
coordinates = (3, 5)
x_pos, y_pos = coordinates

# 함수에서 여러 값 반환
def get_name_age():
    return "김철수", 25

name, age = get_name_age()

# 수정 시도 시 에러
# my_tuple[0] = 100  # TypeError 발생
```



## Range (레인지)

### 정의
- **연속된 정수 시퀀스**를 생성하는 **변경 불가능한** 자료형
- 메모리 효율적 (실제 숫자를 저장하지 않고 규칙만 저장 : 시작 값, 끝 값, 간격)

### 문법
```python
range(stop)           # 0부터 stop-1까지
range(start, stop)    # start부터 stop-1까지
range(start, stop, step)  # start부터 stop-1까지 step 간격으로
```

### 규칙
- stop 값은 **절대 포함되지 않음**
    list(range(5))         # [0, 1, 2, 3, 4]
- step이 양수: start < stop
- step이 음수: start > stop # list(range(5, 0, -1)) -> [5, 4, 3, 2, 1]

### 예시
```python
# 기본 사용법
list(range(5))         # [0, 1, 2, 3, 4]
list(range(2, 8))      # [2, 3, 4, 5, 6, 7]
list(range(0, 10, 2))  # [0, 2, 4, 6, 8]

# 역순
list(range(5, 0, -1))  # [5, 4, 3, 2, 1]
list(range(10, 0, -2)) # [10, 8, 6, 4, 2]

# 반복문에서 활용
for i in range(3):
    print(f"반복 {i}")  # 0, 1, 2

# 리스트 인덱스 순회
my_list = ['a', 'b', 'c', 'd']
for i in range(len(my_list)):
    print(f"인덱스 {i}: {my_list[i]}")
```

## Dict (딕셔너리)

### 정의
- **key-value 쌍**으로 이루어진, **순서와 중복이 없는** **변경 가능한** 자료형
- 중괄호 `{}`로 표현
- '키=밸류 쌍'이 값 하나
- 순서가 없다는 것은 **인덱스가 없다**는 것
- 출력시 개발자의 딕셔너리 입력 순서를 보장해주지만 
  본질은 순서가 없는 자료형이라는 점, key를 통한 접근이라는 점이 핵심

### 키와 값의 규칙
**키(Key)의 규칙:**
- 고유해야 함 (중복 불가)
- 변경 불가능한 자료형만 사용 가능 (str, int, float, tuple)
- 불가능한 타입: list, dict, set

**값(Value)의 규칙:**
- 어떤 자료형이든 사용 가능

### 예시
```python
# 딕셔너리 생성
student = {
    'name': '김철수',
    'age': 20,
    'grades': [85, 90, 78],
    'is_graduated': False
}

empty_dict = {}

# 값 접근
print(student['name'])        # '김철수'
print(student.get('age'))     # 20
print(student.get('height', 0))  # 없는 키는 기본값 반환

# 값 추가/수정
student['major'] = '컴퓨터공학'   # 새 키-값 추가
student['age'] = 21           # 기존 값 수정

# 키-값 삭제
del student['is_graduated']   # 키-값 쌍 삭제
age = student.pop('age')      # 값을 반환하며 삭제

# 딕셔너리 순회
for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"{key}: {value}")

# API 응답 예시 (중첩 딕셔너리)
api_response = {
    'status': 'success',
    'data': {
        'users': [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'}
        ]
    }
}
print(api_response['data']['users'][0]['name'])  # 'Alice'
```



## Set (세트)

### 정의
- 순서와 중복이 없는 **변경 가능한** 자료형
- 중괄호 `{}`로 표현 (빈 값일 땐땐 소괄호: 딕셔너리와 구분)

### 특징
**- 중복 요소 자동 제거
**- 순서가 없음 (인덱싱 불가능)
- 집합 연산 지원

 ### 예시
```python
# 세트 생성
my_set = {1, 2, 3, 4, 5}
empty_set = set()          # 빈 세트 ({}는 빈 딕셔너리)
list_to_set = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# 중복 제거
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers))  # [1, 2, 3, 4, 5]

# 요소 추가/제거
my_set.add(6)       # 요소 추가
my_set.remove(1)    # 요소 제거 (없으면 에러)
my_set.discard(10)  # 요소 제거 (없어도 에러 없음)

# 집합 연산
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)  # 합집합: {1, 2, 3, 4, 5, 6}
print(set1 & set2)  # 교집합: {3, 4}
print(set1 - set2)  # 차집합: {1, 2}
print(set1 ^ set2)  # 대칭차집합: {1, 2, 5, 6}

# 멤버십 테스트 (빠른 검색)
if 3 in my_set:
    print("3이 세트에 있습니다")

# 실제 활용 예시: 중복 제거
email_list = ['a@test.com', 'b@test.com', 'a@test.com', 'c@test.com']
unique_emails = list(set(email_list))
```

## 자료구조 선택 가이드

| 자료구조 | 순서 | 중복 | 변경 | 주요 용도 |
|---------|------|------|------|-----------|
| List | O | O | O | 순서가 중요한 데이터, 인덱스 접근 |
| Tuple | O | O | X | 변경되지 않는 데이터, 함수 반환값 |
| Dict | X | X(키) | O | 키-값 매핑, API 데이터 |
| Set | X | X | O | 중복 제거, 집합 연산 |




# Python 기본 자료형과 연산자 TIL

## 다른 타입

### None
- **정의**: 값이 없음을 나타내는 특별한 값
- **개념**: 빈 상자 (값이 아직 정해지지 않음)
- **주의**: 숫자 0이나 빈 문자열 `''`과는 다름

```python
result = None
print(result)  # None

# 함수가 명시적으로 값을 반환하지 않을 때
def no_return():
    print("hello")

x = no_return()  # x는 None
```

### Boolean
- **정의**: 참(True)과 거짓(False) 단 두 가지 값만 가지는 데이터 타입
- **용도**: 조건문/반복문에서 판단 결과로 사용

```python
is_student = True
is_graduated = False

# 조건문에서 활용
if is_student:
    print("학생입니다")

# 비교 연산 결과
print(5 > 3)    # True
print(10 < 5)   # False
```

## Collection (컬렉션)
여러 개의 값을 담는 보관함

| 컬렉션명 | 변경 가능 여부 | 순서 존재 여부 |
|----------|---------------|---------------|
| str      | X             | O             |
| list     | O             | O             |
| tuple    | X             | O             |
| dict     | O             | X             |
| set      | O             | X             |

## 불변과 가변

### 불변(Immutable) 객체
- str, int, float, tuple, bool, None
- 값을 변경할 수 없음
- 새로운 객체를 생성하여 할당

### 가변(Mutable) 객체
- list, dict, set
- 값을 직접 변경 가능
- 얕은 복사, 깊은 복사 개념과 연관

```python
# 불변 객체
text = "hello"
text += " world"  # 새로운 문자열 객체 생성

# 가변 객체
my_list = [1, 2, 3]
my_list.append(4)  # 기존 객체를 직접 수정
```

## 형변환

### 정의
한 데이터 타입을 다른 데이터 타입으로 변환하는 과정

### 암시적 형변환
파이썬이 자동으로 처리

```python
print(3 + 5.0)      # 8.0 (정수가 자동으로 실수로 변환)
print(True + 3)     # 4 (True가 1로 변환)
print(True + False) # 1 (True=1, False=0)
```

### 명시적 형변환
개발자가 직접 지시

```python
# 문자열을 숫자로
int('123')      # 123
float('3.14')   # 3.14

# 숫자를 문자열로
str(123)        # '123'
str(3.14)       # '3.14'

# 컬렉션 변환
list((1, 2, 3))     # [1, 2, 3]
tuple([1, 2, 3])    # (1, 2, 3)
set([1, 2, 2, 3])   # {1, 2, 3}
```

## 연산자

### 산술 연산자
```python
print(7 + 3)   # 10 (덧셈)
print(7 - 3)   # 4  (뺄셈)
print(7 * 3)   # 21 (곱셈)
print(7 / 3)   # 2.333... (나눗셈)
print(7 // 3)  # 2  (몫)
print(7 % 3)   # 1  (나머지)
print(7 ** 3)  # 343 (거듭제곱)
```

### 복합 연산자
```python
x = 10
x += 3   # x = x + 3, 결과: 13
x -= 2   # x = x - 2, 결과: 11
x *= 2   # x = x * 2, 결과: 22
x //= 3  # x = x // 3, 결과: 7
```

### 비교 연산자
```python
print(5 < 3)    # False (미만)
print(5 <= 5)   # True  (이하)
print(5 > 3)    # True  (초과)
print(5 >= 5)   # True  (이상)
print(5 == 5)   # True  (같음 - 값 비교, 동등성)
print(5 != 3)   # True  (같지 않음)

# is와 == 차이
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  (값이 같음)
print(a is b)   # False (다른 객체)
print(a is c)   # True  (같은 객체)
```

### 논리 연산자
```python
print(True and False)   # False (논리곱)
print(True or False)    # True  (논리합)
print(not True)         # False (논리부정)

# 비교 연산자와 함께 사용
age = 20
print(age >= 18 and age < 65)  # True
```

### 단축 평가 (Short-circuit Evaluation)
논리 연산에서 첫 번째 조건만으로 결과를 판단할 수 있으면 두 번째 조건을 평가하지 않음

```python
# and 연산자의 단축 평가
item1 = '지도'
item2 = '나침반'
result = item1 and item2
print(f'최종적으로 챙긴 물건: {result}')  # 나침반

item1 = '지도'
item2 = ''
result = item1 and item2
print(f'최종적으로 챙긴 물건: "{result}"')  # ""

item1 = ''
item2 = '나침반'
result = item1 and item2
print(f'최종적으로 챙긴 물건: "{result}"')  # ""

# or 연산자의 단축 평가
result = '' or '기본값'
print(result)  # '기본값'

# 실용 예시
name = input("이름을 입력하세요: ") or "익명"
print(f"안녕하세요, {name}님!")
```

### 멤버십 연산자
```python
# in 연산자
print('a' in 'apple')        # True
print(3 in [1, 2, 3, 4])     # True
print('name' in {'name': '김철수', 'age': 20})  # True

# not in 연산자
print('z' not in 'apple')    # True
print(5 not in [1, 2, 3, 4]) # True
```

### 시퀀스형 연산자
```python
# + 결합 연산자 (연결)
print([1, 2] + [3, 4])       # [1, 2, 3, 4]
print('hello' + ' world')    # 'hello world'
print((1, 2) + (3, 4))       # (1, 2, 3, 4)

# * 반복 연산자
print([1, 2] * 3)            # [1, 2, 1, 2, 1, 2]
print('hi' * 3)              # 'hihihi'
print((1, 2) * 2)            # (1, 2, 1, 2)
```

### 트레일링 콤마 (Trailing Comma)
```python
# 리스트/튜플에서 사용 (선택사항)
my_list = [
    1,
    2,
    3,  # 마지막 쉼표 (트레일링 콤마)
]

# 딕셔너리에서 자주 사용
student = {
    'name': '김철수',
    'age': 20,
    'major': '컴퓨터공학',  # 트레일링 콤마
}

# 장점: 새로운 항목 추가 시 편리, 버전 관리에서 깔끔한 diff
```

## 연산자 우선순위
1. `()`  - 괄호
2. `**`  - 거듭제곱
3. `+x`, `-x`, `~x` - 단항 연산자
4. `*`, `/`, `//`, `%` - 곱셈, 나눗셈
5. `+`, `-` - 덧셈, 뺄셈
6. `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `is not`, `in`, `not in` - 비교 연산자
7. `not` - 논리 부정
8. `and` - 논리곱
9. `or` - 논리합