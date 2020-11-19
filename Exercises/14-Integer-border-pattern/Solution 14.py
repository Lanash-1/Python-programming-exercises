'''

Sample input: 

5

Sample output: 

1 2 3 4 5
6 * * * 7
8 * * * 9
10 * * * 11
12 13 14 15 16

'''

N = int(input())                    # initialize a variable N and get the input from the user
count = 1                           # initialize a variable named count and assign its value to 1
for row in range(1, N+1):           # for every row from 1st to N+1th
    for col in range(1, N+1):           # for every column from 1st to N+1th
        if col == 1 or col == N or row == 1 or row == N: # if column is equal to 1 or column is equal to N or row is equal to 1 or row is equal to N
            print(count, end=" ")                           # print the value of count
            count += 1                                      # increase the value of count by 1
        else:                                            # else
            print("*", end=" ")                             # print the symbol '*'
    print()                             # use a empty print statement outside the second for loop for a new line
