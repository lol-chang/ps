n, m = 4,5
res = 0

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
    
    
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            res+=1
print(res)