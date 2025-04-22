l=int(input())
s=list(input())
# print(ord(s[0])-96)
o=0
for index, i in enumerate(s):
    o+=(ord(i)-96) * (31**index)

print(o%1234567891)