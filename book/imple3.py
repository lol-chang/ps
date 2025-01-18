# [1] 문자 input을 인덱스로 사용하기 위한 방법이 최적화 포인트 
# [2] 체스판을 굳이 만들 필요가 없음 !! 
pos = input()
row = int(pos[1])
col = int(ord(pos[0])) - int(ord('a'))+1

steps = [(-2,-1), (-2,1), (2,-1), (2,1), (1,2), (1, -2), (-1,2), (-1,-2)]

result = 0 
for step in steps:
    n_row = row + step[0]
    n_col = col + step[1]
    
    if 1<n_row<=8 and 1<n_col<=8:
        result+=1
        print(n_row, n_col)
print(result)