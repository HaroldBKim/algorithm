n = int(input())
time = list(map(int, input().split()))

time.sort()

result_list = list()
result = 0
for i in range(n):
    result += time[i]
    result_list.append(result)

print(sum(result_list))