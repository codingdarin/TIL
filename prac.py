T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    winner = 0 #무승부는 0
    x = 0

    while x < 6: # 6개뽑을 때까지

        if x%2 ==0:
            player_1.append(arr[x])
            player_1.sort()
        else:
            player_2.append(arr[x])
            player_2.sort()
        
        x += 1        

        if len(player_2) >= 3:
            #런 or 트리플 확인 (플레이어 1부터 체크)
            for i in range(len(player_1)):
                # 먼저 트리플인지
                if player_1.count(player_1[i]) >=3:
                    winner = 1
                    break
                # 런인지
                if i+2 < len(player_1) and player_1[i]+2 == player_1[i+1]+1 == player_1[i+2]:
                    winner = 1
                    break
            for i in range(len(player_2)):
                # 먼저 트리플인지
                if player_2.count(player_2[i]) >=3:
                    winner = 2
                    break
                # 런인지
                if i+2 < len(player_2) and player_2[i]+2 == player_2[i+1]+1 == player_2[i+2]:
                    winner = 2
                    break
        if winner != 0:
            break
            

    print(f"#{tc} {winner}")