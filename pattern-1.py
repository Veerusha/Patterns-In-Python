num = int(input())      # input: 5


# method-1
for i in range(1,num+1):
    for j in range(1,num+1):
        print(j,end=' ')
    print()


# method-2
for i in range(1,num+1):
    for j in range(1,num+1):
        print(i if j==i else j,end=' ')
    print()


# method-3
for i in range(1,num+1):
    for j in range(1,num+1):
        print(num-num+j,end=' ')
    print()




# output:
'''
1 2 3 4 5
1 2 3 4 5 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''