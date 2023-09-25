triangle = []
for i in range(0,3):
    triangle.append(0)

for i in range(0,3):
    triangle[i] = int(input())

sum = 0

for i in range(0,3):
    sum = sum + triangle[i]


if sum != 180:
    print("Error")
elif triangle[0]==triangle[1]==triangle[2]:
    print("Equilateral")
else:
    if triangle[0]==triangle[1]!=triangle[2] or triangle[0]!=triangle[1]==triangle[2] or triangle[0]==triangle[2]!=triangle[1]:
        print("Isosceles")
    elif triangle[0]!=triangle[1]!=triangle[2]:
        print("Scalene")
    


