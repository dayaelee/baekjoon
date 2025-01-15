# 1, 00

n = int(input())

#
# n == 1
# 1
# n == 2
# 00, 11 
# n == 3
# 001, 100, 111 
# n == 4
# 1001, 0011, 1100, 1111, 0000
# n == 5
# 11001, 10011, 00111, 11100, 11111, 10000, 00001, 00000
# #

#n == n-1과 n-2에서 양옆에 1과 00 붙여보기 

dp=[0, 1, 2]

all = [[], [1], ['00', 11]]

for i in range(3, n+1):
    # tmp = []
    # for j in all[i-2]:
    #     #if  i == len(int('00'+str(j))):
    #         tmp.append(('00'+str(j)))
    #         tmp.append((str(j)+'00'))
    # for j in all[i-1]:
    #     #if i == len(int('1'+str(j))):
    #         tmp.append(('1'+str(j)))
    #         tmp.append((str(j)+'1'))
    # all.append(list(set(tmp)))
    #print(all)
    dp.append((dp[i-1]+dp[i-2])%15746)
print(dp[n])
