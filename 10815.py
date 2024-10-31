n = int(input()) # 상근이가 가지고 있는 숫자 카드의 개수
nList = sorted(list(map(int, input().split()))) # 숫자 카드에 적혀있는 정수

m = int(input())
mList = list(map(int, input().split())) 
result=[]
def binarySearch(nList, target, start, end):
    if start>end:
        return 0
    
    mid = (start+end)//2

    if target == nList[mid]:
        return 1
    elif target < nList[mid]:
        return binarySearch(nList, target, start, mid-1)
    else:
        return binarySearch(nList, target, mid+1, end)
 
for i in mList:
    result.append(binarySearch(nList, i, 0, len(nList)-1))

print(' '.join(map(str, result)))