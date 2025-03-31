n=int(input())
nlist = list(map(int, input().split()))
x=int(input())

start = 0
end=n-1
cnt=0
# nList=[]
# for i in range(len(nlist)):
#     nList.append([nlist[i], i])
# print(nList)

nlist.sort()
# print(nList)


while 1:
    if start>end:
        break
    
    
    if nlist[start]+nlist[end]==x and start!=end:
        #print('?', start, end)
        start+=1
        cnt+=1
    elif nlist[start]+nlist[end]>x:
        end-=1
    else:
        start+=1

print(cnt)
    
