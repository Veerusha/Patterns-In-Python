num = int(input())    # num = 5

for i in range(1,num+1):
    p = i
    for j in range(1,num+1):
        print(p, end=' ')
        p+=1
    print()
    

# output
'''
1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
'''