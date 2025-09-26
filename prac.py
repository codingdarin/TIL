n = int(input())
arr = list(map(int, input().split()))
x = int(input())

compare= set()
cnt = 1
for each in arr:
    other = x - each
    if other in compare:
        cnt+=1
    compare.add(each)

print(cnt)