a = input()
a = int(a)
planestr = ""
long_num = a // 4

for i in range(0, long_num):
    planestr = planestr + "long "

print(planestr + "int")