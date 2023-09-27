# n을 기록할 True, False 생성
# 0과 1은 소수가 아니니까 False로 미리 기록
n = 1000000
listTF = [False, False] + [True] * (n-1)

#T가 나온 즉, 소수를 담을 list 생성
primes = []


# 입력받을 a, b 생성
a, b = map(int, input().split())


# Ture, False를 생성할 루틴 
# 2부터 ~ b까지 반복
# 첫번째 자기 자신은 넣고 자기자신의 배수들은 모두 제외 
for i in range(2, b+1):
    if listTF[i]==True:
        # print(i)
        primes.append(i)
        for j in range(i*2, b+1, i):
            listTF[j]=False
            # print("listTF[",j,"]", listTF[j])
            # print("j",j)

# print(primes)

# a부터 b까지 출력 
for i in range(0, len(primes)):
    if primes[i] >= a and primes[i]<=b:
        print(primes[i])

