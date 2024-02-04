N = int(input())
M = N
cycle = 0

while 1: 
    
    cycle += 1
    
    sum = (M // 10) + (M % 10)
    M = (M % 10 * 10) + (sum % 10)
    
    if N == M:
        break

print(cycle)