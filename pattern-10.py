num = int(input())

for i in range(1,num+1):
    p = num
    for j in range(1,num+1):
        print(p,end=' ')
        p-=1
    print()