n = int(input())

initY = 2024
initM = 8

if n>1:
    initY += (initM+(7*(n-1)))//12
    M = (initM+(7*(n-1)))%12
    if M==0:
        M=12
        initY-=1
    print(initY, M)
elif n==1:
    print(2024, 8)
