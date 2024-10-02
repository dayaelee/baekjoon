
n = int(input()) # 소유한 의상 수

closet = {}

for i in range(n):
    r = int(input())
    closet = {}
    for i in range(r):
        value, key = input().split()
        if key in closet:
            closet[key].append(value)
        else:
            closet[key]=[value] 
    sum=1
    if len(closet.keys())==1:
        for i in range(len(closet.keys())):
            tmpList=list(closet.keys())
            tmpkey = tmpList[0]
            print(len(closet[tmpkey]))
            
    else:

        for key, values in closet.items():
            sum*=(len(values)+1)
        print(sum-1)
