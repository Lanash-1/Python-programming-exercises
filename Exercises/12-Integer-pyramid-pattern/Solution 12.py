'''

Sample input: 
 5

 Sample output: 

 * * * * 1
 * * * 1 2 3
 * * 1 2 3 4 5
 * 1 2 3 4 5 6 7
 1 2 3 4 5 6 7 8 9

'''
N = int(input())             # store the input in the variable N
end = 1                      # create a variable end and assign its value to 1
for i in range(1, N+1):      # for i in range from 1 to N+1
    for j in range(N-i):            # for j in range from 0 to N-i
        print("*", end=" ")             # print the symbol '*'
    for k in range(1, end+1):       # for k in range from 1 to end+1
        print(k, end=" ")               # print k
    end += 2                        # increment the value of end by 2
    print()                         # use a empty print statement for creating a new line
