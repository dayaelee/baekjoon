t = int(input())

def calculate(way):
    mid = len(way)//2
    left = way[:mid]
    right = way[mid+1:]
    return left, right

def makeTmpRight(left):
    tmpRight = []
    for i in range(len(left)):
        if left[i]=='1':
            tmpRight.append('0')
        else:
            tmpRight.append('1')
    tmpRight.reverse()
    return tmpRight

def check(way):
    if len(way)==3:
        left, right = calculate(way)
        if (left[0]=='0' and right[0]=='1') or (left[0]=='1' and right[0] =='0'):
            return 
        else:
            realcheck.append(False)
            return 
        
    elif len(way)>3:
        left, right = calculate(way)
        tmpRight = makeTmpRight(left)

        if right == tmpRight:
            check(left)
            check(right)
        else:
            realcheck.append(False)
            return

for i in range(t):
    way = list(input())
    realcheck=[]
    if len(way)==1:
        print('YES')
    else:
        check(way)
        if realcheck:
            print('NO')
        else:
            print('YES')