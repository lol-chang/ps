def get_smallest_node():
    min_value = 999999
    idx = 0

    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i 
    return idx

def basic_dijkstra(start):
    distance[start] = 0 
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost 

n=6
graph = [
    [],
    [(2,2), (4,1), (3,5)],
    [(4,2), (3,3)],
    [(2,3)],
    [(3,3), (5,1)],
    [(3,1), (6,2)],
    [],
]
visited = [False] * (n+1)
distance = [999999] * (n+1)

basic_dijkstra(1)
print(distance)