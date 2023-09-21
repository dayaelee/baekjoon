n = int(input())

str1 = ""
str2 = ""
str3 = ""


str4 = ""
str5 = ""
str6 = ""

m = n
mm = 1
mmm = 1

mn = 1
mmn = n
mmmn = n-1



for i in range(0,n):
    # 상단 
    for j in range(1, m):
        str1= str1+" "

    for k in range(0,mm):
        str2= str2+"*"
    
    if i == 0:
        pass
    else:
        for l in range(0, mmm):
            str3= str3+"*"

    m = m - 1
    mm = mm + 1
    if i == 0:
        pass
    else:
        mmm = mmm + 1
    print(str1+str2+str3)
    str1 = ""
    str2 = ""
    str3 = ""

    #하단 

for i in range(0,n-1):
    for jj in range(0, mn):
        str4 = str4 +" "

    for kk in range(0, mmn-1):
        str5 = str5 +"*"

    for ll in range(0, mmmn-1):
        str6 = str6 +"*"

    mn= mn+1
    mmn= mmn-1
    mmmn= mmmn-1


    print(str4+str5+str6)
    str4 = ""
    str5 = ""
    str6 = ""

