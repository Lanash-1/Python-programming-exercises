'''
Sample input: 

4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Sample output: 

10
26
42
58

'''

row, col = map(int, input().split())   # split the input and assign it to row and col
matrix = []         # create a empty array named matrix
for i in range(row):      # for i in range from 0 to row
    matrix.append(list(map(int, input().split())))      # append the input to the array called matrix
for Row in matrix:        # for each row in matrix
    total = 0             # assign the value of total to 0 
    for n in Row:           # for each number in the row
        total = total + n      # Add the number to total
    print(total)            # print the value of total
