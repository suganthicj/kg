ab,cd=map(str,input().split())
for h in ab:
    for e in cd:
        if h==e:
            flag=0
            break
        else:
            flag=1
    if flag==0:
        break
if flag==0:
    print("yes")
else:
    print("no")
