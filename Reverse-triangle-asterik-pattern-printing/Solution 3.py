'''
Sample Input:

5

Sample Output:

****1
***21
**321
*4321
54321


'''

N = int(input())                        # N represents no of rows
for row in range(1,N+1):                # for each row from 1 to N
    print("*"*int(N-row), end="")       # Print '*' for (No of rows -current row) times
    for number in range(row,0,-1):      # for number in range from current row to 1
        print(number, end="")           # Print the number
    print()                             # empty print statement for creating a new line after each row