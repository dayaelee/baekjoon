n = int(input())

mapp=[[1] * 10 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(8, -1, -1):
        mapp[i][j] = (mapp[i-1][j]+mapp[i][j+1]) % 10007

# for i in mapp:
#     print(i)

print(mapp[n][0])