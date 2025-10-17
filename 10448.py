k = int(input())

t = [1]

while 1:
    tmp = t[-1] + len(t)+1
    if tmp >= 1000:
        break
    t.append(tmp)


for i in range(k):
    n = int(input())

    sum = 0

    tflag = 0
    fflag = 0
    for p in range(len(t)):
        for q in range(len(t)):
            for r in range(len(t)):
                if n== t[p] + t[q] + t[r]:
                    tflag=1
                    break
                elif n<t[p] + t[q] + t[r]:
                    fflag=1
                    break

                # print(t[p], ' ',t[q], ' ', t[r], ' total: ',t[p] + t[q] + t[r], '^^ ', p, ' ',q, ' ', r)
            if tflag==1:
                break


        if tflag ==1:
            break

    if tflag==1:
        print(1)
    else:
        print(0)

                





# while k > 0:



#     k-=1
