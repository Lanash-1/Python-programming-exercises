'''
Sample Input:
3

Sample Output:
3 6 9
2 4 6
1 2 3
'''
N = int(input())				
for row in range(N, 0, -1):
    for elements in range(1,N+1):
        print(row * elements, end=" ")
    print()