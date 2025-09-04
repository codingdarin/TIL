import sys
input = sys.stdin.readline


a, b = map(int, input().split())
while a or b:
    print(a+b)
    a, b = map(int, input().split())


