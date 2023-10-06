# 1.1
print(int(input())%10)

# 1.2
a = input()
ind = a.find(".")
print(a.replace(a[:ind],"0") if ind!=-1 else 0)

# 1.3
a = int(input())
b = int(input())
print(int(b/a)+ (1 if b%a!=0 else 0))
