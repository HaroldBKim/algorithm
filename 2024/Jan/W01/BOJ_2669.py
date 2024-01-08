matrix = [[0] * 100 for _ in range(100 + 1)]

cnt = 0

for i in range(4):
    i, j, x, y = map(int, input().split())
    
    for a in range(i, x): 
        for b in range(j, y):
            if matrix[a][b] == 0:
                matrix[a][b] += 1
                cnt += 1

print(cnt)