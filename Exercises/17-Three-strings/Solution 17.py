'''

Sample input: 

3
JOHN
JOHNY
JANARDHAN

Sample output: 

JJOJAN
OHHARD
NNYHAN

'''

NoOfNames = int(input())   
names = []
for i in range(NoOfNames):
    names.append(input().strip())
for i in range(NoOfNames):
    print((names[i])[:i+1], end="")
print()
for i in range(NoOfNames):
    print((names[i])[i+1:len(names[i])-i-1], end="")
print()
for i in range(NoOfNames):
    print((names[i])[len(names[i])-i-1:], end="")
