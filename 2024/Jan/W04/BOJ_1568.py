n = int(input())

cnt = 1
result = 0

while n >= 1:
    if n < cnt:
        cnt = 1
    
    n = n - cnt
    result += 1
    cnt += 1

print(result)