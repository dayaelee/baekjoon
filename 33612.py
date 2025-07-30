n = int(input())

initY = 2024
initM = 8

if n>1:
    initY += (initM+(7*n))//12
    M = (initM+(7*n))%12
    print(initY, M)
elif n==1:
    print(2024, 8)
