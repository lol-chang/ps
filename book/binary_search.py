
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif  array[mid] < target:
        return binary_search(array, target, mid+1,end)
    else:
        return binary_search(array, target, start,mid-1)
    
def using_for_binarySearch(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start=mid+1
        else:
            end = mid-1
    return None
    

array = [1,2,3,4,5,6,7,8,9]
print(binary_search(array, 5, 0, len(array)))
print(using_for_binarySearch(array, 5, 0, len(array)))