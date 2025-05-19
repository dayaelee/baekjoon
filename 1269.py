a, b = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

# for aa in alist:
#     if aa not in blist:
#         cnta+=1

# for bb in blist:
#     if bb not in alist:
#         cntb+=1

print(len(set(alist)-set(blist))+len(set(blist)-set(alist)))
