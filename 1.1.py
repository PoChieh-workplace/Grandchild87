# 1.1
print(int(input())%10)

# 1.2
a = input()
ind = a.find(".")
print(a.replace(a[:ind],"0") if ind!=-1 else 0)



# 1.4
a = int(input())
tmp = 0
while(a!=0):
    tmp+=a%10
    a/=10
print(tmp)