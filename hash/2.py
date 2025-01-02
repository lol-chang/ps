import sys

# hour와 min을 같이 고려해야 함 
# ex> 10:30 과 11:00인 경우, 문제 발생

# 따라서 같이 고려
s, e, q = input().split()
s = int(s.replace(":", ""))
e = int(e.replace(":", ""))
q = int(q.replace(":", ""))


enter = set()
answer = 0

# 무한 입력 처리 방법 
for line in sys.stdin:
  time, name = line.split()
  time = int(time.replace(":", ""))

  if time <= s:
    enter.add(name)

  if e <= time <= q and name in enter:
    answer += 1
    enter.remove(name)

print(answer)
