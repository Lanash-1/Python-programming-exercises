'''
Sample input: 

5

Sample output: 

----a
---ba
--cba
-dcba
edcba

'''

N = int(input())                   # Store the input in the integer N
alpha = ord('a')                   # store the ascii value of the alphabet 'a' in the varaible named alpha

for i in range(1, N+1):            # for i in range from 1 to N+1
    print("-"*(N-i), end="")            # print the symbol '-' for (N-i)times
    for j in range(1, i+1):             # for j in range from 1 to i+1
        print(chr(alpha), end="")           # print the character equivalent to the value of alpha
        alpha = alpha - 1                   # decrease the value of alpha by 1
    alpha = alpha + (i+1)               # increase the value of alpha by (i+1)
    print()                             # use empty print statement for a new line
