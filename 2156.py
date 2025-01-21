import sys 
input= sys.stdin.readline

n = int(input())
all = [0]+[int(input()) for i in range(n)]

dp=[0]
mdp=[0]

if n >= 1:
    dp.append(all[1])
    mdp.append(all[1])
if n >= 2:
    dp.append(all[1]+all[2])
    mdp.append(all[1]+all[2])
for i in range(3, n+1):
    tmp1 = all[i]+all[i-1]+mdp[i-3]
    tmp2 = all[i]+mdp[i-2]
    dp.append(max(tmp1, tmp2))
    mdp.append(max(dp))

print(max(mdp))

