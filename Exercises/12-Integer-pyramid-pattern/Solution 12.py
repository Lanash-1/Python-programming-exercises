N = int(input())
end = 1
for i in range(1, N+1):
    for j in range(N-i):
        print("*", end=" ")
    for k in range(1, end+1):
        print(k, end=" ")
    end += 2
    print()
