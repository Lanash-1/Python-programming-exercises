'''

Sample input: 

1684285215
3

Sample output: 

568

'''

S = input().strip()
N = int(input())
numbers = []
for n in S:
    if int(n) not in numbers:
        numbers.append(int(n))
numbers.sort()
numbers = numbers[::-1]
result = numbers[:N]
result.sort()
print(*result,sep="")