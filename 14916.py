n = int(input())

first = n//5
flag=0
for i in range(first, -1, -1):
    # print('i', i)
    answer = i
    tmp = n-(5*i)
    # print('tmp', tmp)
    if tmp% 2==0:
        answer += tmp//2
        # print(answer)
        flag=0
        break
    else:
        flag=1
    # print()

if flag==1:
    print(-1)
else:
    print(answer)

# print('answer', answer)
# print('tmp', tmp)
# if tmp% 2==0:
#     answer += tmp//2
#     print(answer)
# else:
#     print(-1)
