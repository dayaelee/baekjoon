'''
N개의 수로 이루어진 수열 A1, A2, ..., AN

또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 

연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)
주어진 수의 순서를 바꾸면 안 된다.

식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 

음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 
그 몫을 음수로 바꾼 것과 같다. 

만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

'''

import sys
import itertools


input = sys.stdin.readline
n = int(input())
ASet = list(map(int, input().split()))
operator = list(map(int, input().split()))

tmp = []

for i in range(len(operator)):
    if i == 0:
        for i in range(operator[i]):
            tmp.append('+')
    elif i == 1:
         for i in range(operator[i]):
            tmp.append('-')
    elif i == 2:
         for i in range(operator[i]):    
            tmp.append('x')
    else:
         for i in range(operator[i]):
            tmp.append('//')

permutations = list(itertools.permutations(tmp))

result = set([])
for i in permutations:
    
    summ=ASet[0]
    check = 0
    for index, j in enumerate(i):
        if j == '+':
            summ+=ASet[index+1]
        elif j =='-':
            summ-=ASet[index+1]
        elif j =='x':
            summ*=ASet[index+1]
        else:
            if summ<0:
                summ=abs(summ)
                summ=summ//ASet[index+1]
                summ = (-summ)
                check =1
            else:
                summ=summ//ASet[index+1]
                
    result.add(summ)
#     print(i, summ)
   

# print(result)
print(max(result))
print(min(result))

