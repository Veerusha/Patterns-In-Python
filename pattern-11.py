num = int(input())

for i in range(1,num+1):
    for j in range(1,num+1):
        print(1 if j==1 or j==num else 0,end=' ')
    print()