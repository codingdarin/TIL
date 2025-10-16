# 큐(Queue) 학습 정리

## 큐의 개념
- **FIFO(First In First Out)**: 선입선출 구조
- 먼저 들어온 데이터가 먼저 나가는 방식
- 일상생활 예시: 은행 번호표, 놀이공원 줄서기

## 큐 vs 스택
- **스택**: LIFO (Last In First Out) - 접시 쌓기
- **큐**: FIFO (First In First Out) - 줄서기

## 큐의 구조
### front(머리)
- 저장된 원소 중 첫 번째 원소를 가리킬 수도 있고
- 첫 번째 원소가 삭제된 위치를 가리킬 수도 있음

### rear(꼬리)  
- 저장된 원소 중 마지막 원소를 가리킬 수도 있고
- 마지막 원소 다음의 빈 위치를 가리킬 수도 있음

## 큐의 주요 연산

| 연산 | 기능 | 설명 |
|------|------|------|
| `createQueue()` | 큐 생성 | 빈 큐를 생성하고 front와 rear를 초기화 |
| `isEmpty()` | 공백 상태 확인 | 큐가 비어있는지 front와 rear의 위치로 판단 |
| `isFull()` | 포화 상태 확인 | 큐가 가득 찼는지 확인 (배열 구현 시) |
| `enqueue(item)` | 원소 삽입 | 큐의 rear(뒤쪽)에 새로운 원소 추가, rear 포인터 이동 |
| `dequeue()` | 원소 삭제 | 큐의 front(앞쪽)에서 원소 제거하고 반환, front 포인터 이동 |
| `peek()` 또는 `front()` | 원소 조회 | 큐의 맨 앞 원소를 제거하지 않고 조회만, 큐는 변경되지 않음 |

## isEmpty()와 isFull()이 함께 존재하는 이유
- **배열 구현**: 고정 크기로 인해 둘 다 필요
- **연결리스트 구현**: isEmpty()만 필요 (메모리 허용 범위 내에서 무제한)

## 배열 큐의 동작 과정

### 1단계: 공백 큐 생성
- front = rear = -1
- 빈 배열 준비

### 2단계: 첫 번째 enqueue(A)
- rear += 1 (rear = 0)
- queue[0] = A
- front는 여전히 -1

### 3단계: 두 번째 enqueue(B)
- rear += 1 (rear = 1)
- queue[1] = B
- front는 여전히 -1

### 4단계: 첫 번째 dequeue()
- front += 1 (front = 0)
- queue[0]의 A를 반환
- rear는 1 그대로

### 5단계: 세 번째 enqueue(C)
- rear += 1 (rear = 2)
- queue[2] = C
- front는 0 그대로

### 6단계: 두 번째 dequeue()
- front += 1 (front = 1)
- queue[1]의 B를 반환
- rear는 2 그대로

### 7단계: 세 번째 dequeue()
- front += 1 (front = 2)
- queue[2]의 C를 반환
- front == rear이므로 큐가 비어있는 상태

## 배열 큐의 문제점
- **공간 낭비** 발생: 앞쪽 공간이 비어있어도 재사용 불가능

## 선형 큐 구현

### 구현 방식
- 배열이나 연결형 리스트로 구현 가능
- 큐의 크기는 배열의 크기와 같음
- front: 가장 최근에 삭제된 원소의 인덱스
- rear: 마지막으로 저장된 원소의 인덱스

### 상태 표현
- **초기 상태**: front = rear = -1
- **공백 상태**: front == rear
- **포화 상태**: rear == n-1 (n: 배열의 크기)

### 선형 큐의 문제점
- **정적 할당**: 처음에 크기를 정하면 변경 불가
- **메모리 낭비**: 실제 사용량보다 크게 할당하면 낭비
- **메모리 부족**: 작게 할당하면 나중에 부족할 수 있음

## 선형 큐의 연산

### enqueue(item) - 삽입 연산
**동작 순서:**
1. rear를 먼저 증가시켜 새로운 원소를 삽입할 자리 지정
2. 증가된 rear 위치에 item 저장

```
enqueue(item):
    global rear
    if is_full(): print("Queue_Full")
    else:
        rear <- rear + 1
        q[rear] <- item
```

### qpeek() - 조회 연산
**기능:** 가장 앞에 있는 원소를 검색하여 반환 (제거하지 않음)

**특징:**
- front+1 위치의 원소를 반환
- front는 삭제된 원소의 위치를 가리키므로 실제 데이터는 front+1에 위치
- 큐의 상태는 변경되지 않음

```python
def qpeek():
    if is_empty(): print("Queue_Empty")
    else: return q[front+1]
```

## 원형 큐(Circular Queue)

### 개념
- 선형 큐의 공간 낭비 문제를 해결하는 방법
- 배열의 끝과 처음을 연결하여 원형으로 사용
- 배열을 시계처럼 원형으로 생각

### 핵심 메커니즘
- **나머지 연산(%) 사용**: `(index + 1) % 배열크기`
- rear가 배열 끝에 도달하면 다시 0번 인덱스로 이동

### 상태 구분 (한 자리 비워두기 방식)
- **공백상태**: `front == rear`
- **포화상태**: `(rear + 1) % n == front`
- **최대 저장 개수**: n-1개 (n: 배열 크기)

### 원형 큐 연산

#### enqueue(item)
```python
def enqueue(item):
    global rear
    if is_full():
        print("Queue Full!")
        return
    rear = (rear + 1) % n  # 원형으로 이동
    queue[rear] = item
```

#### dequeue()
```python
def dequeue():
    global front
    if is_empty():
        print("Queue Empty!")
        return None
    front = (front + 1) % n  # 원형으로 이동
    return queue[front]
```

## 연결 큐(Linked Queue)

### 개념
- 연결리스트를 이용하여 구현한 큐
- 동적 크기 조절 가능
- 메모리 효율적 사용

### 장점
- **동적 크기**: 필요할 때마다 노드 추가/삭제
- **공간 효율**: 실제 사용하는 만큼만 메모리 사용
- **크기 제한 없음**: 메모리가 허용하는 한 무제한
- **포화상태 없음**: 메모리 부족 시까지 계속 추가 가능

### 구조
```
front → [A|→] → [B|→] → [C|None] ← rear
```

### 상태 표현
- **공백상태**: `front == None`
- **포화상태**: 없음 (메모리 부족까지)

### 연결 큐 구현

#### 노드 클래스
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
```

#### enqueue(item)
```python
def enqueue(item):
    global front, rear
    new_node = Node(item)
    
    if rear is None:  # 공백 큐
        front = rear = new_node
    else:
        rear.link = new_node  # 기존 rear와 연결
        rear = new_node       # rear를 새 노드로 이동
```

#### dequeue()
```python
def dequeue():
    global front, rear
    
    if front is None:  # 공백 큐
        print("Queue Empty!")
        return None
    
    data = front.data
    front = front.link  # front를 다음 노드로 이동
    
    if front is None:   # 마지막 노드였다면
        rear = None     # rear도 None으로
    
    return data
```

### 완전한 파이썬 구현
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, item):
        new_node = Node(item)
        
        if self.is_empty():  # 공백 큐
            self.front = self.rear = new_node
        else:
            self.rear.link = new_node  # 기존 rear와 연결
            self.rear = new_node       # rear 이동
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        
        data = self.front.data
        self.front = self.front.link
        
        # 마지막 노드였다면 rear도 None으로
        if self.front is None:
            self.rear = None
            
        print(f"Dequeued: {data}")
        return data
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.front.data
    
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        
        current = self.front
        result = []
        while current:
            result.append(str(current.data))
            current = current.link
        print(" -> ".join(result))
```

## 파이썬에서의 큐 사용

### collections.deque
- **양방향 큐(덱)**: 양방향으로 편리하게 추가와 삭제를 할 수 있는 리스트류 컨테이너
- **연결 리스트를 직접 만들지 않아도 됨**
- **고성능**: `popleft()` 연산이 O(1) (list의 `pop(0)`은 O(n))

```python
from collections import deque

q = deque()
q.append(1)      # enqueue()
t = q.popleft()  # dequeue()
```

### list vs deque 성능 비교
- **list의 pop(0)**: O(n) - 모든 요소를 앞으로 이동
- **deque의 popleft()**: O(1) - 포인터 조작만

## 우선순위 큐(Priority Queue)

### 개념
- **일반 큐**: 들어온 순서대로 나감 (FIFO)
- **우선순위 큐**: 우선순위가 높은 것이 먼저 나감

### 특징
- **삽입**: 아무 위치에나 들어갈 수 있음
- **삭제**: 항상 우선순위가 가장 높은 요소가 나옴

### 구현 방법별 시간복잡도

| 구현 방식 | 삽입 | 삭제 |
|-----------|------|------|
| 정렬되지 않은 배열 | O(1) | O(n) |
| 정렬된 배열 | O(n) | O(1) |
| 정렬되지 않은 연결리스트 | O(1) | O(n) |
| 정렬된 연결리스트 | O(n) | O(1) |
| **힙(Heap)** | **O(log n)** | **O(log n)** |

## 힙(Heap)

### 개념
- **완전 이진 트리** 형태의 자료구조
- 각 노드가 최대 2개의 자식을 가짐

### 힙 속성
- **최대 힙**: 부모 ≥ 자식 (루트가 가장 큰 값)
- **최소 힙**: 부모 ≤ 자식 (루트가 가장 작은 값)

### 배열로 힙 표현
- **부모 인덱스**: `(i-1)//2`
- **왼쪽 자식**: `2*i+1`
- **오른쪽 자식**: `2*i+2`

### 힙의 장점
- **삽입/삭제**: O(log n)
- **최댓값/최솟값 조회**: O(1)

## 배열로 구현한 우선순위 큐

### 정렬되지 않은 배열
```python
class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item, priority):
        self.queue.append((item, priority))  # O(1)
    
    def dequeue(self):
        if not self.queue:
            return None
        
        max_priority_index = 0
        for i in range(len(self.queue)):
            if self.queue[i][1] > self.queue[max_priority_index][1]:
                max_priority_index = i
        
        return self.queue.pop(max_priority_index)  # O(n)
```

### 정렬된 배열
```python
def enqueue(self, item, priority):
    for i in range(len(self.queue)):
        if priority > self.queue[i][1]:
            self.queue.insert(i, (item, priority))  # O(n)
            return
    self.queue.append((item, priority))

def dequeue(self):
    if self.queue:
        return self.queue.pop(0)  # O(1)
```

## 연결리스트로 구현한 우선순위 큐

### 정렬되지 않은 연결리스트
```python
class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

def enqueue(self, data, priority):
    new_node = Node(data, priority)
    new_node.next = self.head  # 맨 앞에 추가 O(1)
    self.head = new_node

def dequeue(self):
    # 최고 우선순위 노드 찾아서 제거 O(n)
    # 전체 순회 필요
```

### 정렬된 연결리스트
```python
def enqueue(self, data, priority):
    new_node = Node(data, priority)
    
    if not self.head or priority > self.head.priority:
        new_node.next = self.head
        self.head = new_node
        return
    
    # 적절한 위치 찾아서 삽입 O(n)
    current = self.head
    while current.next and current.next.priority >= priority:
        current = current.next
    
    new_node.next = current.next
    current.next = new_node

def dequeue(self):
    if not self.head:
        return None
    
    data = self.head.data
    self.head = self.head.next  # O(1)
    return data
```