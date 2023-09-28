e, s, m = map(int, input().split())
ee, ss, mm = 0, 0, 0
count=0
while 1:
    if ee == 16:
        ee = 1

    if ss == 29:
        ss = 1
    
    if mm == 20:
        mm = 1


    if ee == e and ss == s and mm == m:
        print(count)
        break


    ee=ee+1
    ss=ss+1
    mm=mm+1
    count=count+1
   # print(count)
