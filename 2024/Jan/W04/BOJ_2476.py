n=int(input())
res=0
money=0

for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:  # 3개 동일할 경우
        res = 10000 + a * 1000
    elif a == b or b == c:
        res = 1000 + b * 100
    elif c == a:
        res = 1000 + c * 100
    else:
        res = max(a, b, c) * 100

    if res > money:
        money = res

print(money)