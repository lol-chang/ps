# https://www.acmicpc.net/problem/1753

import heapq
# 가중치 최대치가 10이라고 해도 
# INF = 10은 안됨. 가중치의 합을 계산해야 하므로, 10은 INF으로 부족함
INF =  int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a,b,c = map(int, input().split())

    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            # cost = distance[now] + i[1] 가 아니라,
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
