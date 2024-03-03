import sys
input=sys.stdin.readline

N,C=map(int,input().split())

arr=list(map(int,input().split()))
dict={}

for i in range(N):
    if arr[i] in dict:
        dict[arr[i]][0]+=1
    else:
        dict[arr[i]]=[1,i]

dict=sorted(dict.items(),key=lambda x:(-x[1][0],x[1][1]))

for number in dict:
    for num in range(number[1][0]):
        print(number[0],end=" ")