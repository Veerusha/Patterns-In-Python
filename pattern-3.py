num = int(input())      # input: 5
p = 1

for i in range(1,num+1):
    for j in range(1,num+1):
        print(p,end=' ')
        p+=1
    print()


# output:
'''
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''