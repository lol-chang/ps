from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())

    pos = []
    for _ in range(n + 2):
        pos.append(list(map(int, input().split())))
        
    graph = [[] for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(i + 1, n + 2):
            if abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1]) <= 1000:
                graph[i].append(j)
                graph[j].append(i)


    visited = [False] * (n + 2)
    queue = deque([0]) 
    visited[0] = True
    found = False  

    while queue:
        current = queue.popleft()
        if current == n + 1:
            print("happy")
            found = True
            break
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    if not found:
        print("sad")
