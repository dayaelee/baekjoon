n = int(input())
n2=n
n3=n
result3=0
count3=0
result2=0
count2=0
result=0
count=0

while(1):
  if n3==1:
    break
  elif n3<1:
    break

  if n3%3==0:
    result+=n3//3
    count+=1
    n3=n3//3
    if n3==1:
      break
  else:
    n3-=1
   #print(n)
    result+=1
    count+=1

while(1):
  if n==1:
    break
  elif n<1:
    break

  if n%3==0:
    if n%2==0:
      if n//3<n//2:
        result3+=n//3
        count3+=1
        n=n//3
        continue
      else: 
        result3+=n//2
        count3+=1
        n=n//2
        continue
    result3+=n//3
    count3+=1
    n=n//3
    if n==1:
      break
  elif n%2==0:
    result3+=n//2
    count3+=1
    n=n//2
  else:
    n-=1
   #print(n)
    result3+=1
    count3+=1
  
while(1):
  if n2==1:
    break
  elif n2<1:
    break
    
  if n2%2==0:

    result2+=n2//2
    count2+=1
    n2=n2//2
    if n2==1:
      break
  else:
    
    n2-=1
    result2+=1
    count2+=1
 

if count2>=count3:
  if count3>count:
    print(count)
  else:
    print(count3)
elif count3>=count2:
  if count2>count:
    print(count)
  else:
    print(count2)
elif count2==0 and count3==0:
  print('0')