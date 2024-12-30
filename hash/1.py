n = int(input())

res = set()

for _ in range(n):
    name, action = input().split()

    if action == 'enter':
        res.add(name)

    else:
        res.remove(name)


for name in sorted(res, reverse=True):
    print(name)
