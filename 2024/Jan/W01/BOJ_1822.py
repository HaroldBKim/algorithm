a,b = map(int,input().split()) 

ab1 = set(list(map(int,input().split()))) 
ab2 = set(list(map(int,input().split())))

res = ab1 - ab2 

print(len(res)) 

if len(res) > 0:
    for i in sorted(res): 
        print(i,end=" ")