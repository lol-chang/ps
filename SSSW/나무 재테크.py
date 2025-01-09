# https://www.acmicpc.net/problem/16235

n, m, k = map(int, input().split())

nutrient = []
for _ in range(n):
    nutrient.append(list(map(int, input().split())))

tree = [[[] for _ in range(n)] for _ in range(n)] 
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

di = [1, 1, 1, 0, 0, -1, -1, -1]
dj = [1, -1, 0, 1, -1, 1, -1, 0]

ground = [[5 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    die_tree = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            live_trees = []
            for t in sorted(tree[i][j]):
                if ground[i][j] >= t:
                    ground[i][j] -= t
                    live_trees.append(t+1)
                else: # 죽은 나무 표시 
                    die_tree[i][j] += t // 2 
            tree[i][j] = live_trees

    # 죽은 나무 제거 후, 양분 추가 
    for i in range(n):
        for j in range(n):
            ground[i][j] += die_tree[i][j]
    
    
    # 나무 번식 
    for i in range(n):
        for j in range(n):
            for t in tree[i][j]:
                if t % 5 == 0:
                    for k in range(8):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if 0<=ni<n and 0<=nj<n:
                            tree[ni][nj].append(1)

    

    # ground에 양분 추가 
    for i in range(n):
        for j in range(n):
            ground[i][j] += nutrient[i][j]

res = 0
for i in range(n):
    for j in range(n):
        res += len(tree[i][j])
            
print(res)