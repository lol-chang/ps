n, k = map(int, input().split())

from collections import deque

def bfs(start, target):
    max_limit = 100000
    visited = [False] * (max_limit + 1)

    q = deque([(start, 0)])
    visited[start] = True

    while q:
        pos, time = q.popleft()

        if pos == target:
            return time
        
        # range 아님 주의 
        for n in (pos-1, pos+1, pos*2):
            if 0 <= n <= max_limit and not visited[n]:
                visited[n] = True
                q.append((n, time+1))

print(bfs(n,k))
