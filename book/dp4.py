n, m = map(int, input().split())
x=[]
for _ in range(n):
    x.append(int(input()))

# 이 문제 생각하기 실패~~! 
#####
d = [10001] * (m+1)
d[0]=0
#####

#####
for i in x:
    for j in range(i, m+1):
        d[j] = min(d[j], d[j-i]+1)
#####
if d[m]==10001:
    print(-1)
else:
    print(d[m])