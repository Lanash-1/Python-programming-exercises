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

NoOfRows = int(input())                 # Get NoOfRows from the user
for row in range(1,NoOfRows+1):             # for each row till last row
    for element in range(1,row+1):       # for element in range from 1 to row
        print(element, end = " ")        # print the element
    print()                          # use a empty print statement to create a empty line   