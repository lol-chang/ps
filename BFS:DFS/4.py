from collections import deque

def bfs(graph, i, j):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque([(i,j)])
    size = 0 

    while q:
        x, y = q.popleft()
        
        if graph[x][y] == 1:
            graph[x][y] = 0 
            size += 1  

        for i in range(4):
            nx, ny  = x + dx[i], y + dy[i]
            
            if 0 < nx <= n and 0 < ny <= n and graph[nx][ny] == 1:
                q.append((nx,ny))

    return size

def dfs(i,j):
    if i<0 or j < 0 or i >= n or j >= n:
        return 0
    if graph[i][j]==1:
        graph[i][j]=0  #방문처리 
        size = 1
        size += dfs(i-1, j)
        size += dfs(i+1, j)
        size += dfs(i, j-1)
        size += dfs(i, j+1)
        return size
    return 0
        

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

res = []
for i in range(n):
    for j in range(n):

        size = bfs(graph, i, j)
        
        # DFS 
        #size = dfs(i,j)

        if size > 0:
            res.append(size)

res.sort()
print(len(res))
for i in res:
    print(i)