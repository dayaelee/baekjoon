sum = 0.0
count = 0
for i in range (0, 20):
    a, b, c = input().split(" ")
    b = float(b)
    fc= 0.0

    if c == "A+":
        fc = 4.5
    elif c == "A0":
        fc = 4.0
    elif c == "B+":
        fc = 3.5
    elif c == "B0":
        fc = 3.0
    elif c == "C+":
        fc = 2.5
    elif c == "C0":
        fc = 2.0
    elif c == "D+":
        fc = 1.5
    elif c == "D0":
        fc = 1.0
    elif c == "F":
        fc = 0.0
    else :
        fc = 0.0
        # P의 경우 

    if c != "P":
        # print("b*fc: ", b*fc)
        sum = sum + (b * fc)
        # print("sum: ", sum)
        count = count+b

    else:
        pass


# print("sum: ", sum)
# print("count: ", count)


print(round((sum/count), 6))


