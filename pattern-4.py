num = int(input())    # num = 5
p = num*num

for i in range(1,num+1):
    for j in range(1,num+1):
        print(p,end=' ')
        p-=1
    print()
 

# output:   
'''
25 24 23 22 21 
20 19 18 17 16 
15 14 13 12 11 
10 9 8 7 6
5 4 3 2 1
'''