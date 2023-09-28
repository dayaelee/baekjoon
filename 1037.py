n = int(input())
aList=[]

aList = list(map(int, input().split()))

aList.sort()

if(len(aList)==n):
        if(len(aList)==1):
            print(aList[0]*aList[0])
        else:
            print(aList[0]*aList[-1])
    
