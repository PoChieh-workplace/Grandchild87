# 1.7
a = int(input())
match a:
    case a if a<0:
        print(-1)
    case a if a==0:
        print(0)
    case _:
        print(1)