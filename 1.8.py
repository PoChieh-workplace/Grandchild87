# 1.8
a = int(input())
print("LEAP" if a%400==0 else ("COMMON" if a%100==0 else ("LEAP" if a%4==0 else "COMMON"))) 