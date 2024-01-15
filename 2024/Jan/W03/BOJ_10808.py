alnum = [0]*26
for i in input():
    alnum[ord(i)-97] += 1
print(*alnum)