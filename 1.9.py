lists = [int(i) for i in input().split(" ")]
dx,dy = (lists[0]-lists[2],lists[1]-lists[3])
if dx==0 or dy==0 or abs(dx)==abs(dy):
    print("YES")
else:
    print("NO")