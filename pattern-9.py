num = int(input())    # num = 5

for i in range(1,num+1):
    p = i*i
    for j in range(1,num+1):
        print(p,end=' ')
        p+=1
    print()

# output
'''
1 2 3 4 5 
4 5 6 7 8 
9 10 11 12 13
16 17 18 19 20
25 26 27 28 29
'''