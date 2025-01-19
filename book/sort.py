array = [3,5,2,1]

def selected_sort():
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    print(array)


def insert_sort():
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    print(array)



def quick_sort(array, start, end):
    if start >= end:
        return 
    
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # pivot보다 큰 값 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left+=1
        while right > start and array[right] >= array[pivot]:
            right-=1
        
        if left>right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)


# ===>
def quick(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick(left_side) + [pivot] + quick(right_side)
print("Python 최적화 quick sorting")
print(quick(array))


# 계수 정렬은 요소값의 최대값만큼의 list를 사용해야 하므로,
# 범위를 알 수 있는 정수형일 때, 사용 가능 (매우 유리)
def count_sort():
    count = [0] * (max(array)+1)

    for i in range(len(array)):
        count[array[i]] += 1
    
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')
print("계수정렬은 바로 리스트 요소값을 정렬시키는게 아니긴 함")
count_sort()