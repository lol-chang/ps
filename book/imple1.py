n = int(input())

x,y = 1,1

comm = list(map(str, input().split()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for c in comm:
    for i in range(len(move_types)):
        if c == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 파이썬 변수 스코프가 좀 이상하네..        
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
        
    x,y = nx,ny
print(x,y)
