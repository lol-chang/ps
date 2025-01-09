
def dust_stread():
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    spread_dust = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if graph[x][y] == -1:
                continue
            if graph[x][y] != 0:
                spot_count = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0<=nx<r and 0<=ny<c and graph[nx][ny]!=-1:
                        spot_count+= 1
                        spread_dust[nx][ny] += graph[x][y] // 5
                graph[x][y] -= (graph[x][y] // 5) * spot_count
                
    
    for x in range(r):
        for y in range(c):
            graph[x][y] += spread_dust[x][y]


# 회전 시키는거 구현력이 부족해서 GPT씀 ㅠ
# 오랜만이라, 이런건 못하네 연습 필수 
def cleaning():
    # 공기청정기의 위치
    upper_cleaner, lower_cleaner = clean_pos[0], clean_pos[1]

    # 1. 위쪽 공기청정기의 반시계 방향 순환
    # 아래로 이동
    for i in range(upper_cleaner - 1, 0, -1):
        graph[i][0] = graph[i - 1][0]
    # 왼쪽으로 이동
    for i in range(c - 1):
        graph[0][i] = graph[0][i + 1]
    # 위로 이동
    for i in range(upper_cleaner):
        graph[i][c - 1] = graph[i + 1][c - 1]
    # 오른쪽으로 이동
    for i in range(c - 1, 1, -1):
        graph[upper_cleaner][i] = graph[upper_cleaner][i - 1]
    # 공기청정기에서 나오는 바람 처리
    graph[upper_cleaner][1] = 0

    # 2. 아래쪽 공기청정기의 시계 방향 순환
    # 위로 이동
    for i in range(lower_cleaner + 1, r - 1):
        graph[i][0] = graph[i + 1][0]
    # 왼쪽으로 이동
    for i in range(c - 1):
        graph[r - 1][i] = graph[r - 1][i + 1]
    # 아래로 이동
    for i in range(r - 1, lower_cleaner, -1):
        graph[i][c - 1] = graph[i - 1][c - 1]
    # 오른쪽으로 이동
    for i in range(c - 1, 1, -1):
        graph[lower_cleaner][i] = graph[lower_cleaner][i - 1]
    # 공기청정기에서 나오는 바람 처리
    graph[lower_cleaner][1] = 0


r, c, t = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))

for _ in range(t):
    dust_stread()
    
    clean_pos = []
    for i in range(r):
        if graph[i][0]==-1:
            clean_pos.append(i)
    
    cleaning()

res= sum(graph[x][y] for x in range(r) for y in range(c) if graph[x][y] > 0)
print(res)