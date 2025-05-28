import sys
n, k = map(int, input().split())
alist=list(map(int, input().split()))

def merge_sort(targetList, k):
    global cnt
    if len(targetList)<=1:
        return targetList

    mid = (len(targetList)+1)//2

    l = targetList[:mid]
    r = targetList[mid:]
    # print(l, r)

    
    ll = merge_sort(l, k)
    rr = merge_sort(r, k)
        
    
    result=[]
    i, j = 0, 0
    while i< len(ll) and j <len(rr):
        if ll[i]<=rr[j]:
            result.append(ll[i])
            ans.append(ll[i])
            i+=1
            
        else:
            result.append(rr[j])
            ans.append(rr[j])
            j+=1
    
    while i < len(ll):
        result.append(ll[i])
        ans.append(ll[i])
        i+=1
    while j < len(rr):
        result.append(rr[j])
        ans.append(rr[j])
        j+=1

    return result
ans=[]
merge_sort(alist, k)
# print(ans)
if k <= len(ans):
    print(ans[k-1])
else:
    print(-1)