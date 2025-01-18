n, k = map(int, input().split())

# 간단한 로직(1씩 감소)이라, Input이 크면 timeout이다. 
def my():
    cnt = 0
    while True:
        if n == 1:
            break

        if n % k == 0:
            n = n // k 
        else:
            n-=1 
        cnt += 1 
    print(cnt)

# 입력값이 100억 이상일 시, 유용
def optimize():
    res = 0
    while True:
        target = (n//k) * k 
        res += (n-target)
        n = target
        
        if n < k:
            res += n-1 
            print(res)
            break
        
        n //= k 
        res += 1 
