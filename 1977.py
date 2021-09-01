short=int(input())
max=int(input())

start = 1
sum=0
bb=[]

while(1):
    n_start = start * start
    if(n_start<short):
        start=start+1
        continue
    elif(n_start>=short and n_start<=max):
        sum=n_start+sum
        bb.append(int(sum))
        start=1+start
        a=n_start
        continue
    elif(n_start>max):
        if(sum==0):
            print('-1')
            break
        else:
            print(sum)
            print(bb[0])
            break
        break
    else:
        break
