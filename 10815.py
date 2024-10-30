'''
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

'''

n = int(input()) # 상근이가 가지고 있는 숫자 카드의 개수
nList = sorted(list(map(int, input().split()))) # 숫자 카드에 적혀있는 정수

# print('nList', nList)

m = int(input())
mList = list(map(int, input().split())) 
# 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수
result=[]
def binarySearch(nList, target, start, end):
    if start>end:
        return 0
    
    mid = (start+end)//2
    # print('mid', mid, 'target', target)

    if target == nList[mid]:
        return 1
    elif target < nList[mid]:
        return binarySearch(nList, target, start, mid-1)
    else:
        return binarySearch(nList, target, mid+1, end)
 
for i in mList:
    # print('')
    # print(binarySearch(nList, i, 0, len(nList)-1))
    result.append(binarySearch(nList, i, 0, len(nList)-1))
    # print(result)

print(' '.join(map(str, result)))