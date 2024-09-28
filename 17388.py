tmp = list(map(int, input().split()))

if ((tmp[0]+tmp[1]+tmp[2]>=100)):
    print("OK")
else:
    a=min(tmp[0], tmp[1],tmp[2])

    for i in range(3):
        if a== tmp[i]:
            if i == 0:
                print("Soongsil")
            elif i == 1:
                print("Korea")
            elif i == 2:
                print("Hanyang")

            

