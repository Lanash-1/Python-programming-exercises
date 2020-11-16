'''

Sample input:

5

Sample output: 

1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5

'''

N = int(input())                 # Store the no of number of rows in the variable N
for row in range(1,N+1):             # for each row till Nth row
    for element in range(1,row+1):       # for element in range from 1 to row
        print(element, end = " ")        # print the element
    print()                          # use a empty print statement to create a empty line   