# BOJ 16928. 뱀과 사다리 (D3 / G5)
#------------------------------------------------1회차 풀이
# 사다리랑 뱀만 인접리스트에 넣기?

import sys
from collections import deque

input = sys.stdin.readline
arr = [0]*101
N, M = map(int, input().split())

for _ in range(N):
    s, e = map(int, input().split())
    arr[s] = e

for _ in range(M):
    s, e = map(int, input().split())
    arr[s] = e

visited = [0] *101
q = deque([1,])

# 이동 시작 (BFS)
current = 0
for dice in range(1,7):
    next_pos = current + dice
    if next_pos < 100:
        if arr[next_pos] != 0:
            next_pos = arr[next_pos]

        if not visited[next_pos]:



