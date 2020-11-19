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

N = int(input())
count = 1
for row in range(1, N+1):
    for col in range(1, N+1):
        if col == 1 or col == N or row == 1 or row == N:
            print(count, end=" ")
            count += 1
        else:
            print("*", end=" ")
    print()
