'''

Sample input: 

3 6
24

Sample output: 

3 6 9 12 15 18 21
21 18 15 12 9 6 3

'''

N1, N2 = map(int, input().split())
N3 = N1 + N2
limit = int(input())
numbers = []
for i in range(N1, limit):
    if i%N1 == 0 or i%N2 == 0 or i%N3 == 0:
        if i not in numbers:
            numbers.append(i)
print(*numbers)
print(*numbers[::-1])