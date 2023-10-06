# 1.4
a = int(input())
tmp = 0
while(a!=0):
    tmp+=a%10
    a = round(a/10)
print(tmp)