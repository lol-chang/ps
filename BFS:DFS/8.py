f, s ,g, u, d = map(int, input().split())

visited = [False] * (f+1)


from collections import deque
def bfs(start, target):
    
    q = deque([(start, 0)])
    visited[start] = True

    while q:
        pos, count = q.popleft()

        if pos == target:
            return count
        
        for next_pos in (pos + u, pos - d):
            if 1 <= next_pos <= f and not visited[next_pos]:
                    visited[next_pos] = True
                    q.append((next_pos, count+1))
    
    return "use the stairs"

print(bfs(s, g))