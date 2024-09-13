n = int(input())

for i in range(n):
    h, w, n = map(int, input().split())
    oneT=n//h
    last= n%h

    #print('last: ', last,'oneT:',  oneT)



    '''
    1//1 = 1  => one
    last 1 % 1 == 0 => last

    10//6 == 1 => one
    10%6 == 4  => last


    1
    1 10 10 
    => 110

    10 // 1 == 1 => one
    10 % 1 == 0 => last

    
    1
    10 10 100

    100//10 = 10 => one
    100%10 = 0 => last

    3 66 28
    28//3 = 9 => one
    28%3 = 1 => last

    4 27 38
    38//4 = 9 => one
    38%4 = 2 => last

    '''

    
    if last ==0:
        if oneT>=10:
            oneT=str(oneT)
            #print("!")
        else:
            oneT='0'+str(oneT)
            #print("!!")
        if h ==1:
            last = 1
            #print("!!!")
        else:
            last = h
            #print("!!!!")

    else:
        if w >= n:
            if oneT+1>=10:
                oneT=str(oneT+1)
                #print("!!!!!!")
            else:
                oneT='0'+str(oneT+1)
                #print("!!!!!")
        else:
            if oneT+1>=10:
                oneT=str(oneT+1)
                #print("!!!!!!")
            else:
                oneT='0'+str(oneT+1)
                #print("!!!!!!!")
    
    result = str(last)+str(oneT)
    print(result)