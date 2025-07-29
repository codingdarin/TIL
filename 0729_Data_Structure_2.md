# 딕셔너리 메서드

## .get(key[, default])
키에 해당하는 값을 반환. 키가 없으면 default 값 반환 (기본값: None)

```python
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))        # Alice
print(person.get('height'))      # None
print(person.get('height', 0))   # 0

# person[key]와 비슷하지만, person['height'] 하면 에러가 나서 프로그램이 멈출 수 있음
# 에러 시 멈추면 안 될 때와 에러 반응을 확인해야 할 때를 구분해서 적절한 걸로 사용 가능


```

## .keys()
딕셔너리의 모든 키를 반환하는 뷰 객체. **실시간으로 동기화됨**

```python
person = {'name': 'Alice', 'age': 25}
keys_view = person.keys()
print(keys_view)  # dict_keys(['name', 'age'])

# 새로운 키 추가하면 keys_view도 자동 변경
person['city'] = 'Seoul'
print(keys_view)  # dict_keys(['name', 'age', 'city'])

# 리스트로 변환
print(list(person.keys()))  # ['name', 'age', 'city']

# 반복문으로 키 출력
for key in person.keys():
    print(key)
```

## .values()
딕셔너리의 모든 값을 반환하는 뷰 객체. keys()와 동일한 방식으로 동작

```python
person = {'name': 'Alice', 'age': 25}
print(person.values())  # dict_values(['Alice', 25])

# 반복문으로 값 출력
for value in person.values():
    print(value)
```

## .items()
딕셔너리의 키-값 쌍을 튜플로 반환하는 뷰 객체

```python
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])

# 반복문에서 튜플 언패킹으로 키, 값 분리
for key, value in person.items():
    print(f"{key}: {value}")
```

# 딕셔너리 메서드

## .get(key[, default])
키에 해당하는 값을 반환. 키가 없으면 default 값 반환 (기본값: None)

```python
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))        # Alice
print(person.get('height'))      # None
print(person.get('height', 0))   # 0
```

## .keys()
딕셔너리의 모든 키를 반환하는 뷰 객체. **실시간으로 동기화됨**

```python
person = {'name': 'Alice', 'age': 25}
keys_view = person.keys()
print(keys_view)  # dict_keys(['name', 'age'])

# 새로운 키 추가하면 keys_view도 자동 변경
person['city'] = 'Seoul'
print(keys_view)  # dict_keys(['name', 'age', 'city'])

# 리스트로 변환
print(list(person.keys()))  # ['name', 'age', 'city']

# 반복문으로 키 출력
for key in person.keys():
    print(key)
```

## .values()
딕셔너리의 모든 값을 반환하는 뷰 객체. keys()와 동일한 방식으로 동작

```python
person = {'name': 'Alice', 'age': 25}
print(person.values())  # dict_values(['Alice', 25])

# 반복문으로 값 출력
for value in person.values():
    print(value)
```

## .items()
딕셔너리의 키-값 쌍을 튜플로 반환하는 뷰 객체

```python
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])

# 반복문에서 튜플 언패킹으로 키, 값 분리
for key, value in person.items():
    print(f"{key}: {value}")
```

## .pop(key[, default])
키를 제거하고 연결된 값을 반환. 키가 없으면 KeyError 발생하거나 default 반환

```python
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))     # 25
print(person)                # {'name': 'Alice'}

# default 값 지정
print(person.pop('country', 'Unknown'))  # Unknown

# default 없이 존재하지 않는 키 접근시 에러
# print(person.pop('country'))  # KeyError: 'country'
```

## .clear()
딕셔너리의 모든 키/값 쌍을 제거

```python
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)  # {}
```

## .setdefault(key[, default])
키와 연결된 값을 반환. **키가 없다면 default 값으로 새 키를 딕셔너리에 추가하고 default 반환**

```python
person = {'name': 'Alice', 'age': 25}

# 기존 키: 값만 반환, 딕셔너리 변경 없음
print(person.setdefault('name', 'Bob'))  # Alice
print(person)  # {'name': 'Alice', 'age': 25}

# 새 키: 딕셔너리에 추가하고 default 값 반환
print(person.setdefault('city', 'Seoul'))  # Seoul
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Seoul'}

# default 생략시 None으로 설정
print(person.setdefault('country'))  # None
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Seoul', 'country': None}
```


## .update([other])
other가 제공하는 키/값 쌍으로 딕셔너리를 갱신. **기존 키는 덮어씀 (마지막 값이 유지됨)**

```python
person = {'name': 'Alice', 'age': 25}

# 다른 딕셔너리로 업데이트
other_dict = {'age': 30, 'city': 'Seoul'}
person.update(other_dict)
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'Seoul'}

# 키워드 인수로 업데이트
person.update(name='Bob', country='Korea')
print(person)  # {'name': 'Bob', 'age': 30, 'city': 'Seoul', 'country': 'Korea'}

# 키/값 쌍의 시퀀스로 업데이트
person.update([('age', 35), ('job', 'Developer')])
print(person)  # {'name': 'Bob', 'age': 35, 'city': 'Seoul', 'country': 'Korea', 'job': 'Developer'}
```

### 키로 사용 가능한 자료형 (hashable)
```python
# 불변 자료형만 키로 사용 가능
data = {
    'string_key': 'value1',     # 문자열
    42: 'value2',               # 정수
    3.14: 'value3',             # 실수
    (1, 2): 'value4',           # 튜플
    True: 'value5'              # 불린
}

# 함수도 키로 사용 가능
def my_func():
    return "hello"

data[my_func] = 'function_value'
```

### 키로 사용 불가능한 자료형 (unhashable)
```python
# 가변 자료형은 키로 사용 불가
# data = {[1, 2]: 'value'}      # 에러! 리스트
# data = {{}: 'value'}          # 에러! 딕셔너리  
# data = {set(): 'value'}       # 에러! 집합
```

**참고:** update()는 키-값 쌍 구조를 받아야 하므로 단순 문자열은 직접 사용 불가능



# 세트(Set)

## 개요
고유한 항목들의 정렬되지 않은 컬렉션

- **해시 테이블**을 사용하여 데이터 저장
- 항목의 **고유성을 효율적으로 보장**
- 항목 추가, 삭제, 존재여부 확인 등이 **매우 빠름**
- **집합 연산**을 간편하게 수행 가능

## 기본 사용법
```python
# 세트 생성
my_set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}

# 중복 제거됨
duplicate_set = {1, 2, 2, 3, 3, 3}
print(duplicate_set)  # {1, 2, 3}

# 빈 세트 생성 (주의: {}는 딕셔너리)
empty_set = set()
print(empty_set)  # set()

# 리스트에서 세트 생성
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}
```

## 세트의 특징
- **순서 없음**: 인덱스로 접근 불가능
- **중복 불허**: 동일한 값은 하나만 저장
- **가변**: 항목 추가/삭제 가능
- **해시 가능한 요소만 저장**: 리스트, 딕셔너리 등은 요소로 사용 불가

```python
# 해시 가능한 요소들
valid_set = {1, 'hello', (1, 2), True}

# 해시 불가능한 요소는 에러
# invalid_set = {[1, 2]}  # TypeError: unhashable type: 'list'
```


# 세트(Set)

## 개요
고유한 항목들의 정렬되지 않은 컬렉션

- **해시 테이블**을 사용하여 데이터 저장
- 항목의 **고유성을 효율적으로 보장**
- 항목 추가, 삭제, 존재여부 확인 등이 **매우 빠름**
- **집합 연산**을 간편하게 수행 가능

## 기본 사용법
```python
# 세트 생성
my_set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}

# 중복 제거됨
duplicate_set = {1, 2, 2, 3, 3, 3}
print(duplicate_set)  # {1, 2, 3}

# 빈 세트 생성 (주의: {}는 딕셔너리)
empty_set = set()
print(empty_set)  # set()

# 리스트에서 세트 생성
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}
```

## 세트의 특징
- **순서 없음**: 인덱스로 접근 불가능
- **중복 불허**: 동일한 값은 하나만 저장
- **가변**: 항목 추가/삭제 가능
- **해시 가능한 요소만 저장**: 리스트, 딕셔너리 등은 요소로 사용 불가

```python
# 해시 가능한 요소들
valid_set = {1, 'hello', (1, 2), True}

# 해시 불가능한 요소는 에러
# invalid_set = {[1, 2]}  # TypeError: unhashable type: 'list'
```

## 순서 보장하며 중복 제거 (실무 팁)
**세트는 순서를 보장하지 않으므로**, 순서가 중요한 경우 다른 방법 사용

```python
# 문제에서 자주 나오는 패턴: 순서 유지하며 중복 제거
original = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# 방법 1: 딕셔너리 사용 (Python 3.7+)
result1 = list(dict.fromkeys(original))
print(result1)  # [3, 1, 4, 5, 9, 2, 6]

# 방법 2: 반복문으로 직접 구현
result2 = []
for item in original:
    if item not in result2:
        result2.append(item)
print(result2)  # [3, 1, 4, 5, 9, 2, 6]

# 세트로만 하면 순서 깨짐
result3 = list(set(original))
print(result3)  # [1, 2, 3, 4, 5, 6, 9] (순서 변경됨)
```

## 세트 메서드

### .add(x)
세트에 요소 x를 추가

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# 이미 있는 요소 추가해도 변화 없음
my_set.add(2)
print(my_set)  # {1, 2, 3, 4}
```

### .update(iterable)
반복 가능한 객체의 모든 요소를 세트에 추가

```python
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])
print(my_set)  # {'c', 2, 3, 1, 'b', 4, 5, 'a'}

# 문자열도 가능
my_set.update('xyz')
print(my_set)  # {'c', 2, 3, 1, 'b', 4, 5, 'a', 'x', 'y', 'z'}
```

### .clear()
세트의 모든 요소를 제거

```python
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # set()
# 주의: 빈 세트는 {}가 아닌 set()로 표현됨 ({}는 딕셔너리)
```

### .remove(x)
세트에서 요소 x를 제거. **요소가 없으면 KeyError 발생**

```python
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)  # {1, 2, 4, 5}

# 없는 요소 제거 시 에러
# my_set.remove(10)  # KeyError: 10
```

### .pop()
세트에서 **임의**의 요소를 제거하고 반환 (임의 ≠ 무작위/랜덤)

```python
my_set = {1, 2, 3, 4, 5}
removed = my_set.pop()
print(f"제거된 요소: {removed}")  # 제거된 요소: 1 (예시)
print(my_set)  # {2, 3, 4, 5}

# 빈 세트에서 pop() 시 에러
# empty_set = set()
# empty_set.pop()  # KeyError: 'pop from an empty set'
```

### .discard(x)
세트에서 요소 x를 제거. **remove()와 달리 요소가 없어도 에러 없음**

```python
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print(my_set)  # {1, 2, 4, 5}

# 없는 요소 제거해도 에러 없음
my_set.discard(10)
print(my_set)  # {1, 2, 4, 5} (변화 없음)
```

## 세트의 집합 메서드

| 메서드 | 연산자 | 설명 | 예시 |
|--------|--------|------|------|
| `set1.difference(set2)` | `set1 - set2` | set1에만 있고 set2에는 없는 요소들 (차집합) | `{1,2,3} - {2,3,4}` → `{1}` |
| `set1.intersection(set2)` | `set1 & set2` | set1과 set2 모두에 있는 요소들 (교집합) | `{1,2,3} & {2,3,4}` → `{2,3}` |
| `set1.issubset(set2)` | `set1 <= set2` | set1이 set2의 부분집합인지 확인 | `{1,2} <= {1,2,3}` → `True` |
| `set1.issuperset(set2)` | `set1 >= set2` | set1이 set2를 포함하는지 확인 (상위집합) | `{1,2,3} >= {1,2}` → `True` |
| `set1.union(set2)` | `set1 \| set2` | set1과 set2의 모든 요소들 (합집합) | `{1,2} \| {3,4}` → `{1,2,3,4}` |

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 차집합
print(set1.difference(set2))    # {1, 2}
print(set1 - set2)              # {1, 2}

# 교집합
print(set1.intersection(set2))  # {3, 4}
print(set1 & set2)              # {3, 4}

# 부분집합 확인
subset = {1, 2}
print(subset.issubset(set1))    # True
print(subset <= set1)           # True

# 상위집합 확인
print(set1.issuperset(subset))  # True
print(set1 >= subset)           # True

# 합집합
print(set1.union(set2))         # {1, 2, 3, 4, 5, 6}
print(set1 | set2)              # {1, 2, 3, 4, 5, 6}
```

## 참고: 해시 테이블

### 정의
**키와 값을 짝지어 저장하는 자료구조**
* 해시: 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것

### 해시 테이블의 원리
1. **키를 해시 함수를 통해 해시값으로 변환**
2. **변환된 해시값을 인덱스로 삼아 데이터를 저장하거나 찾음**
3. **이로 인해 검색, 삽입, 삭제를 매우 빠르게 수행** (평균 O(1))

* 해시 함수: 임의 길이 데이터를 입력 받아 고정 길이(정수)로 변환해 주는 함수. 이 정수가 바로 해시 값

| 키 | 해시 함수 | 해시값(인덱스) | 버킷(저장공간) |
|----|-----------|--------------:|----------------|
| "apple" | hash("apple") | 2 | [bucket 2] |
| "banana" | hash("banana") | 5 | [bucket 5] |
| "cherry" | hash("cherry") | 1 | [bucket 1] |

```
키 → 해시 함수 → 해시값(인덱스) → 버킷(저장공간)
```


## set의 요소 & dict의 키와 해시 테이블 관계

### set
- 각 요소를 해시 함수로 변환한 나온 해시 값에 맞춰 해시 테이블 내부 버킷(bucket)에 위치시킴
- 그래서 "순서" 라기보다 "버킷 위치(인덱스)"가 요소의 위치를 결정
- 따라서 set는 **순서를 보장하지 않음**

### dict
- 키(key) → 해시 함수 → 해시 값 → 해시 테이블에 저장
- 단 set와 달리 "삽입 순서"는 유지한다는 것이 언어 사양에 따라 보장 됨 (Python 3.7 이상)
- 즉, 키를 추가한 순서대로 반복문 순회할 때 나오게 됨
- **사용자에게 보여지는 키 순서는 삽입 순서가 유지되도록 설계된 것

### 핵심 차이점
```python
# set - 순서 보장 안됨
my_set = {3, 1, 4, 2}
print(my_set)  # 순서가 보장되지 않음

# dict - 삽입 순서 유지 (Python 3.7+)
my_dict = {'c': 3, 'a': 1, 'd': 4, 'b': 2}
print(my_dict)  # {'c': 3, 'a': 1, 'd': 4, 'b': 2} - 삽입 순서 유지
```

* 근데 정수는 해시값이 정수 그대로

### Python에서의 활용
```python
# 딕셔너리 - 해시 테이블 구조
dict_example = {"apple": 5, "banana": 3, "cherry": 8}
print(dict_example["apple"])  # O(1) 시간에 접근

# 세트 - 해시 테이블 구조 (값만 저장)
set_example = {"apple", "banana", "cherry"}
print("apple" in set_example)  # O(1) 시간에 확인

# 리스트와 비교 - 순차 탐색 필요
list_example = ["apple", "banana", "cherry"]
print("apple" in list_example)  # O(n) 시간 소요
```

**따라서** 딕셔너리와 세트가 빠른 이유는 **해시 테이블** 덕분!


### 파이썬에서의 해시 함수
- 정수
  - 같은 정수는 항상 같은 해시값
- 문자열
  - 문자열 해시 시 파이썬 인터프리터 시작 때 설정되는 난수 시드가 달라질 수 있음
  - 보안상 이유로 해시 난수호 도입
  - 각 실행마다 'a'의 해시 값도 매번 바뀔 수 있음


## set의 요소 & dict의 키와 해시테이블 관계

### set의 pop()은 "임의의 요소"를 제거하고 반환함
- **실행할 때마다 다른 요소를 얻는다는 의미에서의 "무작위"가 아니라**
- **"임의"는 의미에서의 "무작위"** (by "arbitrary" the docs don't mean "random")

### 내부적으로 해시 테이블(버킷)을 참조하기 때문에, 실행 때마다 다른 요소가 먼저 나올 수 있음
- **해시 난수화로 인해 문자열 같은 해시 값이 실행마다 달라질 수 있고,**
- **따라서 set 내부 요소의 배치가 달라질 수 있음**

### 정수는 해시 값이 항상 동일하기 때문에, 파이썬을 동일 프로세스에서 연속 실행할 때는 결과가 어느 정도 일정해 보이기도 하지만, 여전히 set은 순서가 없으므로 pop()되는 순서는 예측 불가능

```python
# 실행할 때마다 다를 수 있음
my_set = {'apple', 'banana', 'cherry'}
print(my_set.pop())  # 실행마다 다른 요소가 나올 수 있음

# 정수는 비교적 일정해 보이지만 여전히 순서 보장 안됨
num_set = {1, 2, 3, 4, 5}
print(num_set.pop())  # 예측 불가능
```

### 핵심
**pop()의 "임의"는 "무작위"가 아닌 "예측할 수 없는 순서"를 의미**하며, 
해시 테이블 구조상 어떤 요소가 먼저 나올지 보장되지 않음


set 요소 & dict 키는 해시 가능(hashable)한 객체만 저장 가능

이유

해시 테이블은 객체의 해시값을 인덱스로 사용
가변 객체는 내용이 변경되면 해시값도 달라짐
해시값이 변하면 저장된 위치를 찾을 수 없게 됨



-----

파이썬 문법 규격
EBNF
백어스나우르 폼 확장판

서로 다른 프로그래밍 언어, 데이터 형식, 프로토콜 등의 문법을 통일하여 정의하기 위함

