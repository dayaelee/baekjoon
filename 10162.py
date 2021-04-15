a=int(input())
b=a
count = 0
strr=''
result=0

array=[300, 60, 10]

for i in array:
  if i!=300:
    strr+=' ' #문자열부분

  if a//i>0:
    count += a // i
    c=a//i
    result+=c*i
    a%=i
    strr+= str(c)
  #해당 버튼으로 돌려 줄 수 있는 버튼의 누름수 세기 
  else:
    strr+='0'


if result==b:
  print(strr)
else:
  print(-1)  
