n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))
ans = []
# XOR; 두 입력이 서로 다를때만 1 같을 때 0
nu=[0, ]

for i in range(1, n+1):
    # if i ==0:
    #     nu.append(a[i])
    # else:
        nu.append(nu[i-1]^a[i])

# ans = []

answer=0
for i in range(q):
    s, e = map(int, input().split())
    # ans.append(nu[e-1]^nu[s-2])
    answer ^= (nu[e]^nu[s-1])

# answer=0
# for i in range(len(ans)):
#     if i ==0:
#         answer=ans[i]
#     else:
#         answer=answer^ans[i]
print(answer)

