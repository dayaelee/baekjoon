n = int(input())
count=0
if n//100000000>=1:
   count = count+((n-100000000)+1)*9
   count = count+((99999999-10000000)+1)*8
   count = count+((9999999-1000000)+1)*7
   count = count+((999999-100000)+1)*6
   count = count+((99999-10000)+1)*5
   count = count+((9999-1000)+1)*4
   count = count+((999-100)+1)*3
   count = count + ((99-10)+1)*2
   count = count + 9
   print(count)
elif n//10000000>=1:
   count = count+((n-10000000)+1)*8
   count = count+((9999999-1000000)+1)*7
   count = count+((999999-100000)+1)*6
   count = count+((99999-10000)+1)*5
   count = count+((9999-1000)+1)*4
   count = count+((999-100)+1)*3
   count = count + ((99-10)+1)*2
   count = count + 9
   print(count)
elif n//1000000>=1:
   count = count+((n-1000000)+1)*7
   count = count+((999999-100000)+1)*6
   count = count+((99999-10000)+1)*5
   count = count+((9999-1000)+1)*4
   count = count+((999-100)+1)*3
   count = count + ((99-10)+1)*2
   count = count + 9
   print(count)
elif n//100000>=1:
   count = count+((n-100000)+1)*6
   count = count+((99999-10000)+1)*5
   count = count+((9999-1000)+1)*4
   count = count+((999-100)+1)*3
   count = count + ((99-10)+1)*2
   count = count + 9
   print(count)
elif n//10000>=1:
   count = count+((n-10000)+1)*5
   count = count+((9999-1000)+1)*4
   count = count+((999-100)+1)*3
   count = count + ((99-10)+1)*2
   count = count + 9
   print(count)
elif n//1000>=1:
   count = count+((n-1000)+1)*4
   count = count+((999-100)+1)*3
   count = count + ((99-10)+1)*2
   count = count + 9
   print(count)
elif n//100>=1:
   count = count+((n-100)+1)*3
   count = count + (((99-10)+1)*2)
   count = count + 9
   print(count)
elif n // 10 >=1:
   count = count + (((n-10)+1)*2)
   count = count + 9
   print(count)
elif n // 10 == 0 and n % 10 >= 1:
   count = count + n
   print(count)
   

