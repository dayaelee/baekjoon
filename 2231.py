n = int(input())

ten = 10
c = 0
cc=0
sum = 0


while 1:
    if cc >= ten**7 and cc < ten ** 8:
        sum += cc // (ten ** 7) # 자릿수 추가
        cc = cc % (ten ** 7)

    if cc >= ten**6 and cc < ten ** 7:
        sum += cc // (ten ** 6) # 자릿수 추가
        cc = cc % (ten ** 6)

    if cc >= ten**5 and cc < ten**6:
        sum += cc // (ten ** 5)
        cc = cc % (ten ** 5)
    
    if cc >= ten**4 and cc < ten** 5:
        sum += cc // (ten ** 4)
        cc = cc % (ten ** 4)
    
    if cc >= ten**3 and cc < ten ** 4:
        sum += cc // (ten ** 3)
        cc = cc % (ten ** 3)

    if cc >= ten**2 and cc < ten ** 3:
            sum += cc // (ten ** 2)
            cc = cc % (ten ** 2)
            
    if cc >= ten**1 and cc < ten ** 2:
            sum += cc // (ten ** 1)
            cc = cc % (ten ** 1)
            
    if cc >= 0 and cc < 10:
            sum += cc
            
            if sum == n :
                    print(c)
                    break
            
            else:
                    if c>=n:
                        print(0)
                        break
                        
                    # else:
                        #print("cc",cc)
                        
                        #print(c)
                    sum=0
                    c=c+1
                    cc=c
                    sum += c

            
    

           

     

