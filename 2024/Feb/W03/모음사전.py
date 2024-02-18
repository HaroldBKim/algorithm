from itertools import product as pr
def solution(word):
    alpha_list = ['A', 'E', 'I', 'O', 'U']
    dict_list = []
    for i in range(1, 6): 
        pr_results = pr(alpha_list, repeat = i)
        for r in pr_results: 
            dict_list.append(''.join(r)) 
    dict_list.sort()
    return dict_list.index(word) + 1