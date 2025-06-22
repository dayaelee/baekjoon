n = int(input())
x = int(input())

# print(n-(n*0.01*x))
now = n*(1-(0.01*x))

print(round(((100*(n-now))/now),6))
