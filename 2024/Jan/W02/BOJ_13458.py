N = int(input())    				
A = list(map(int, input().split()))  
B, C = map(int, input().split())     
cnt = 0 

for i in A: 
    if i <= B:      
        cnt += 1    
        continue    
        
    i -= B         
    cnt += 1       
    
    if i % C == 0: 
        cnt += i//C
        
    else :          
        cnt += i//C + 1

print(cnt) 