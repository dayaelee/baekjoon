n = int(input())
if n==1:
    print(1)
elif n>=2 and n<=7:
     print(2)
else:
    a=2
    b=7
    i=1
    while 1:
            a=a+(6*i)
            b=b+(6*(i+1))
            #print("i", i, "a", a, "b", b)
            if n>=a and n<=b:
                print(i+2)
                break
            i = i+1

    