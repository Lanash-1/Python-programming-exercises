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

N = int(input())
alpha = ord('a')
for i in range(1, N+1):
    print("-"*(N-i), end="")
    for j in range(1, i+1):
        print(chr(alpha), end="")
        alpha = alpha - 1
    alpha = alpha + (i+1)
    print()
