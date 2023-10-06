# 1.1
print(int(input())%10)

# 1.2
a = input()
ind = a.find(".")
print(a.replace(a[:ind],"0") if ind!=-1 else 0)

# 1.3