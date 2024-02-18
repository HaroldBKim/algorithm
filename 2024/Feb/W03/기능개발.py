from math import ceil
def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        days.append(ceil((100-p)/s)) 
        
    res = [] 
    max = 0 
    for i in range(1, len(days)) :
        if days[i] > days[max] : 
            res.append(len(days[max:i])) 
            max = i 
        if i == len(days)-1 : 
            res.append(len(days[max:])) 
    return res          