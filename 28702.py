from collections import deque
target=[]
for i in range(3):
    target.append(input())

for i in range(2, -1, -1):
    if target[i].isdigit():
        next = int(target[i])+(3-i)
        break

if next % 15==0:
    print('FizzBuzz')
elif next % 3==0:
    print('Fizz')
elif next % 5==0:
    print('Buzz')
else:
    print(next)
    