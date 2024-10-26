'''
a0=1

'''
import collections
a = collections.defaultdict(int)

n, p, q = map(int, input().split())

# cntN = 1

# o=int(n//p)
# t=int(n//q)

# a[0]=1

# def dp(i, p, q):
#     if a[i] != 0:
#         return a[i]
    
#     a[i] = dp(i//p, p, q) + dp(i//q, p, q)
#     return a[i]

# print(dp(n, p, q)) 


# for i in range(cntN, n+1):

#     o=int(i//p)
#     t=int(i//q)
#     value =  a[o]+a[t]
#     print('a[o]+a[t]', a[o], a[t], a[o]+ a[t])
#     a[i] = value
#     remValue = value


# print(a)
a[0]=1

def dp(i, p, q):
    if a[i] != 0:
        return a[i]
    a[i] = dp(int(i/p), p, q) + dp(int(i/q), p, q)
    return a[i]

print(dp(n, p, q)) 