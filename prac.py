from collections import deque

def solve(N, M):
    if N >= M:
        return N - M  # -1 연산만 사용
    
    visited = [False] * 1000001  # 숫자 방문 체크
    queue = deque([(N, 0)])  # (현재값, 연산횟수)
    visited[N] = True
    
    while queue:
        current, cnt = queue.popleft()
        
        if current == M:
            return cnt
        
        # 4가지 연산
        operations = [current + 1, current - 1, current * 2, current - 10]
        
        for next_val in operations:
            if 1 <= next_val <= 1000000 and not visited[next_val]:
                visited[next_val] = True
                queue.append((next_val, cnt + 1))
    
    return -1  # 도달 불가능

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = solve(N, M)
    print(f"#{tc} {result}")

