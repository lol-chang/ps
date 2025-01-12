import heapq

n, k = map(int, input().split())

INF = int(1e9)
distance = [INF]  * 100001


q = []
heapq.heappush(q, (0, n))

while q:
    cost, pos = heapq.heappop(q)
    
    if distance[pos] < cost:
        continue

    if pos == k:
        print(cost)
        break

    for next_pos, move_cost in [(pos-1, 1), (pos+1, 1), (pos*2, 0)]:
        if 0 <= next_pos < 100001:
            new_cost = cost + move_cost
            if new_cost < distance[next_pos]:
                distance[next_pos] = new_cost
                heapq.heappush(q, (new_cost, next_pos))

# 초기 코드인데, 그래프 안쓰는 다익스트라 or BFS 탐색 연습 시급 ! 
# import heapq

# n, k = map(int, input().split())

# INF = int(1e9)
# distance = [INF]  * 100001


# q = []
# heapq.heappush(q, (0, n))

# while q:
#     cost, pos = heapq.heappop(q)
    
#     if pos == k:
#         print(cost)
#         break

#     if pos - 1 >= 1 and distance[pos-1]==INF:
#         heapq.heappush(q, (cost+1, pos-1))
#     if pos + 1 < k+1 and distance[pos+1]==INF:
#         heapq.heappush(q, (cost+1, pos+1))
#     if 1<=pos*2 < k+1:
#         heapq.heappush(q, (min(distance[pos*2], cost), pos*2))
