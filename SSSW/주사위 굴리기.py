# https://www.acmicpc.net/problem/14499

# 최적화가 아쉽긴 한데, 구현은 성공함 
n,m,x,y,k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

command = list(map(int, input().split()))

dice = [0] * 7
res = []
for c in command:

    if c == 1: # 동
        if y + 1 < m:
            dice[2], dice[5] = dice[5], dice[2]
            dice[1], dice[2] = dice[2], dice[1]
            dice[1], dice[6] = dice[6], dice[1]

            y += 1 
        else:
            continue
        
    elif c==2: # 서
        if y - 1 >= 0:
            dice[2], dice[1] = dice[1], dice[2]
            dice[2], dice[5] = dice[5], dice[2]
            dice[5], dice[6] = dice[6], dice[5]
            
            y -= 1
        else:
            continue

    elif c==3: # 북
        if x - 1 >= 0:
            dice[3], dice[2] = dice[2], dice[3]
            dice[2], dice[4] = dice[4], dice[2]
            dice[4], dice[6] = dice[6], dice[4]

            x -= 1 
        else:
            continue

    else: #남 
        if x + 1 < n:
            dice[4], dice[2] = dice[2], dice[4]
            dice[2], dice[3] = dice[3], dice[2]
            dice[3], dice[6] = dice[6], dice[3]

            x += 1 
        else:
            continue

    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y]
        graph[x][y] = 0 
    print(dice[2])

