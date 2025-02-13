# ========================================================================================
# 이진탐색 사용

# # n = int(input())
# a = list(map(int,input().split()))
# m = int(input())
# b = list(map(int,input().split()))

# a.sort()
# b.sort()
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2

#         if array[mid] == target:
#             return 1
#         elif array[mid] < target:
#             start = mid+1
#         else:
#             end=mid-1
#     return 0


# start = 0 
# end = len(a)

# for i in a:
#     if binary_search(a, i, start, end)== 0:
#         print("no")
#     else:
#         print("yes")

# ========================================================================================
# 계수 정렬 이용

# n = int(input())
# arr = [0] * 1000001

# for i in input().split():
#     arr[int(i)] = 1

# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if arr[i] == 1:
#         print("yes")
#     else:
#         print("no")

# ========================================================================================    
# 집합 자료형 사용

n = int(input())
a = set(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))

for i in b:
    if i in a:
        print("yes")
    else:
        print("no")