N = int(input())
names = []
for i in range(N):
    names.append(input().strip())
for i in range(N):
    print((names[i])[:i+1], end="")
print()
for i in range(N):
    print((names[i])[i+1:len(names[i])-i-1], end="")
print()
for i in range(N):
    print((names[i])[len(names[i])-i-1:], end="")
