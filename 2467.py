n=int(input())
nl=list(map(int, input().split()))

left=0
right=n-1
result=float('inf')
resultSet=[]
while left<right:
    sum=nl[left]+nl[right]
    # print('sum', sum)
    if result>abs(sum):
        result=abs(sum)
        resultSet.append([nl[left], nl[right]])

    if sum>0:
        right-=1
    if sum==0:
        break

    if sum<0:
        left+=1
print(' '.join(map(str,resultSet[-1])))