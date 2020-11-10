'''
Sample input 1:
123

Sample output 1: 
244

Sample input 2: 
789

Sample output 2:
800
'''

N = input().strip()                 # Get the input from the user as a string and assign it to the variable N

for number in N:                                 # for each number in N
    if int(number) == 8 or int(number) == 9:     # if the number is equal to 8 or 9
        print("0", end="")                       # then print '0' 
    elif int(number)%2 == 0:                     # or if the number is even
        print(int(number) + 2, end="")           # then print (number+2)
    else:                                        # else
        print(int(number) + 1, end="")           # print (number+1)