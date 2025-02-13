def binary_search(array, target, start, end):
    res = 0
    while start <= end:
        total = 0
        mid = (start+end)//2
        
        for x in array:
            if x > mid:
                total += x - mid

        if total < target:
            end = mid-1
        else:
            res = mid
            start = mid+1
    return res
    
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
print(binary_search(array, m, start, end))


