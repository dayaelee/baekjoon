import math

ax, ay, az=map(int, input().split())
cx, cy, cz=map(int, input().split())


# print(az + bx, ay * by, ax + bz)

# cx-az = bx
# cy //ay= by
# cz-ax =  bz
print(cx-az ,cy //ay,  cz-ax )