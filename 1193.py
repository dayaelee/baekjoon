x = int(input())
if(x==1):
    print(str(1)+"/"+str(1))
else:

    i = 1
    a = 0
    b = 0

    count=1
    sum=1
    start2=1
    holzzak=0 #홀 1 짝 0
    for i in range(2, 10000000):
        if i == 2:
            count=count+i
        else:
            count=count+i


        if(sum+(i-1)<=x and count>=x):
            #print("i:",i,",",  sum+(i-1), "<= x <=", count)
            num = x-(sum+(i-1))+1
            if(i%2==0):#짝수면
                a=start2
                b=i
                holzzak = 0
                break
            else: #홀수면 
                a=i
                b=start2
                holzzak = 1
                break
        sum = i-1 + sum

    # print("num",num)
    # print("no problem")
    # print("holzzak", holzzak)
    # print("a:", a, "b:", b)

    cnt=1
    while 1:
        if(num==cnt):
                print(str(a)+"/"+str(b))
                break
        if holzzak==0:
            a=a+1
            b=b-1
        else:
            a=a-1
            b=b+1
        cnt+=1