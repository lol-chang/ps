# 이 구현 문제 생각보다 제대로 못풀었음.. 다시 해보기
# 구현 어려웠던 이유
# 1) 진행 방향 구현 미숙
# 2) 후진 
# 3) 회전 방향 구현 뇌정지 
# ==> 어려운 부분은 아니라 익숙해지면 될 둣 

n, m = map(int,input().split())
x, y, d = map(int, input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
visited[x][y] = True
count = 1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d==-1:
        d=3
    

turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if not visited[nx][ny] and graph[nx][ny]==0:
        visited[nx][ny] = True
        x, y = nx, ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    
    if turn_time==4:
        # 뒤로 가기를 이렇게 구현하네 
        nx = x - dx[d]
        ny = y - dy[d]
        
        if graph[nx][ny]==1:
            break
        else:
            x,y=nx,ny
            turn_time=0
print(count)

        

