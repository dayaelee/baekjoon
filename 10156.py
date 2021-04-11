n = input().split()
K=int(n[0])
N=int(n[1])
M=int(n[2])

need= K*N

if need>M:
  print(need-M)
else:
  print('0')
