n = int(input())
res = 0

for _ in range(n):
    x = input()
    res += list(x) == sorted(x, key=x.find)
print(res)