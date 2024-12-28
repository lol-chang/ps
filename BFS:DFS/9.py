import sys
from collections import deque 

input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

max_value = max(max(row) for row in graph)
min_value = min(min(row) for row in graph)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(h, x , y, visited):
    if visited[x][y] or graph[x][y] <= h:
        return 0

    q = deque([(x,y)])
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] <= h or visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            q.append((nx, ny))

    return 1 


# 아무것도 안잠기는 경우도 있을 수 있다.
# 이 경우가 for문으로는 왜 안되는 것인가
# res = [1]  
# range(min_value - 1, ...) 으로 해줘야 하는데

# 이게 없으면,

# 3
# 1 1 1
# 1 1 1
# 1 1 1
# 강수량이 0인 경우(모든 지역이 남아 있음):
#     안전 영역은 1이어야 함 (모든 지역이 연결되어 있음).
# 강수량이 1 이상인 경우:
#     안전 영역은 0이어야 함 (모든 지역이 잠김).

# 이 경우에서 안전지역을 최대로 구해야 하므로! 강수량 없는 경우(min_value -1 or res = [1])을 고려해줘야 함 !! 

res = [1]

for h in range(min_value, max_value+1):
    tmp = 0
    visited = [[False] * n for i in range(n)]
    for x in range(n):
        for y in range(n):
            tmp += bfs(h, x, y, visited)
    res.append(tmp)

print(max(res))

