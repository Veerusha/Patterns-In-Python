num = int(input())    # num = 5

# method-1
for i in range(1,num+1):
    for j in range(1,num+1):
        print(i if i%2!=0 else num-j+1, end=' ')
    print()


# method-2
for i in range(1,num+1):
    for j in range(1,num+1):
        print(i if i%2==1 else num-j+1, end=' ')
    print()


# output
'''
1 1 1 1 1 
5 4 3 2 1
3 3 3 3 3
5 4 3 2 1
5 5 5 5 5
'''