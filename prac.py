# 동철이의 일 분배

def give_task(person, cur_prob, used):
    global ans
    
    # 가지치기: 현재 확률이 이미 답보다 작거나 같으면 종료
    if cur_prob <= ans:
        return
    
    # 종료 조건: 모든 사람에게 일 배정 완료
    if person == N:
        ans = max(ans, cur_prob)
        return

    for task in range(N):
        # 비트마스크로 사용 여부 체크
        if not (used & (1 << task)):
            # 해당 작업을 사용으로 표시
            give_task(person + 1, cur_prob * arr[person][task] / 100, used | (1 << task))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    ans = 0
    give_task(0, 1.0, 0)  # 초기 비트마스크는 0
    
    print(f"#{tc} {ans * 100:.6f}")