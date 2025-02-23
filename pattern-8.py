num = int(input())    # num = 5

# method-1
for i in range(num,0,-1):
    for j in range(1,num+1):
        print(i if i%2==1 else j, end=' ')
    print()

# method-2
for i in range(1,num+1):
    for j in range(1,num+1):
        print(j if i%2==0 else num-i+1, end=' ')
    print()


# output
'''
5 5 5 5 5 
1 2 3 4 5
3 3 3 3 3
1 2 3 4 5
1 1 1 1 1
'''