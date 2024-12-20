n = int(input())

dp=[0, 0]



for i in range(2, n+1):
    
    c1 = dp[i-1] +1
    if i % 2==0 and i % 3 !=0:
        c2 = dp[i//2] + 1
        dp.append(min(c1, c2))
    elif i % 2 !=0 and i % 3==0:
        c3 = dp[i//3] + 1
        dp.append(min(c1, c3))
    elif i % 2==0 and i % 3 ==0:
        c2 = dp[i//2] + 1
        c3 = dp[i//3] + 1
        dp.append(min(c1, c2, c3))
    elif i % 2!=0 and i % 3 !=0:
        dp.append(c1)
print(dp[n])
        
        

