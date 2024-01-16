N = int(input())
M = int(input())
li = sorted(list(map(int, input().split())))
ans = 0
s, e = 0, len(li)-1

while s != e:
    if li[s] + li[e] == M:
        ans += 1
        e -= 1
    elif li[s] + li[e] < M:
        s += 1
    elif li[s] + li[e] > M:
        e -= 1
        
print(ans)