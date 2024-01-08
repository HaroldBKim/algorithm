H, W = map(int, input().split())
area = [list(input()) for _ in range(H)]

cloud_time = 1 
is_cloud = False 

for i in range(H):
    for j in range(W):

        if area[i][j] == 'c': 
            area[i][j] = 0
            is_cloud = True
            cloud_time = 1

        elif area[i][j] == '.' and is_cloud == False: 
            area[i][j] = -1

        elif area[i][j] == '.' and is_cloud == True: 
            area[i][j] = cloud_time
            cloud_time += 1

    cloud_time = 1
    is_cloud = False
    print(*area[i])
