num = int(input())      # input: 5

# method-1
for i in range(1,num+1):
    for j in range(1,num+1):
        print(j if i%2==1 else num-j+1,end=' ')
    print()


# method-2
for i in range(1,num+1):
    for j in range(1,num+1):
        print(num-j+1 if i%2==0 else j,end=' ')
    print()



# output:
'''
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
'''