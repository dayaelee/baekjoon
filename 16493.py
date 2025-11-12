n, m = map(int, input().split())


chapters=[]
for i in range(m):
    chapters.append(list(map(int, input().split())))

cnt = 0

answer =0

bag = [[0 for _ in range(n+1)] for _ in range(m+1)]

# print(chapters)

for i in range(1, m+1):
    for j in range(n+1):
        if chapters[i-1][0]<=j:
            bag[i][j]=max(chapters[i-1][1]+bag[i-1][j-chapters[i-1][0]], bag[i-1][j])
        else:
            bag[i][j]=bag[i-1][j]

# for k in bag:
#     print(k)


print(bag[m][n])