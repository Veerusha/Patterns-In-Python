num = int(input())      # input: 5


# method-1
for i in range(1,num+1):
    for j in range(1,num+1):
        print(num-j+1,end=' ')
    print()
    

# method-2
for i in range(1,num+1):
    for j in range(num,0,-1):
        print(j,end=' ')
    print()
    

# method-3
for i in range(num,0,-1):
    for j in range(num,0,-1):
        print(j,end=' ')
    print()



# output:
'''
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''