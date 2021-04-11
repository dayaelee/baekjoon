n = input()
hicount= n.count('-')
n1= n.split('-')
result=''

for i in range(hicount+1):
  result+=n1[i][0]
print(result)
