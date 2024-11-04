# '''


# '''

# n = int(input())

# basic='666'
# check = 0
# littleCNT=0
# double = 0
# for i in range(n):
#     if i == 0:
#         print(basic)
#         cnt=1
#     else:
#         if cnt%10!=6:
#             total=int(str(cnt)+basic)
#             print(total)
#             cnt+=1
#         elif cnt%10==6:
            
#             if littleCNT==0:
#                 # target='6'
#                 print('double', 'cnt', double, cnt)
#                 # for i in range(double):
#                 #     target+='6'
#                 total=int(str(cnt)+basic)-cnt
#                 print('hi', total)
#             else:
#                 total+=1
#                 print('a', total)
#             littleCNT+=1
#             if littleCNT==10*len(str(cnt)):
#                 double+=1
#                 total = str(total)
#                 cnt+=1
#                 if int(total)>=10000:
#                     #print('total', int(total)%10000)
#                     total=str(int(total)%10000)
#                 # if len(total)>=4:
#                 #     for i in range(len(total)-4):
#                 #         total=total[1:]
#                 #         print('hi totoa', total)
#                 total=str(cnt)+total[:-1]
#                 print(total)
#                 littleCNT=0
#                 cnt+=1
#         #print('cnt', cnt)
        
N = int(input())

def moviePD():
    answer = 0
    num = 666
    while True:
        if '666' in str(num):
            answer += 1
            if answer == N:
                return num
        num += 1

print(moviePD())
