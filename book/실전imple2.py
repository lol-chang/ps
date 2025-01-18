x = input()

text = []
num = []

for k in x:
    if k.isalpha():
        text.append(k)
    else:
        num.append(k)

print(''.join(sorted(text))+ str(sum(map(int, num))))