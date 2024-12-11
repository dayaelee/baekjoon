n = int(input())
listA=sorted(list(map(int,input().split())))
m = int(input())
listB = list(map(int, input().split()))

#print(listA)
def check(start, end, i):
    #print('start end, i', start, end, i)
    if start >= end:
        return 0

    target=(start+end)//2
    if listA[target] < i:
        start = target
        return check(start, end, i)
    elif listA[target] > i:
        end = target
        return check(start, end, i)
    elif listA[target] == i:
        return 1

for i in listB:
    start = 0
    end = len(listA)
    if i > listA[end-1]:
        print(0)
    else:
        result=check(start, end, i)
        print(result)
        
    