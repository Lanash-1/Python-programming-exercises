'''
Check the image for the problem statement and Sample input and output
'''

N = int(input())
files = []
for i in range(N):
    files.append(input().strip())
duplicate = []
for i in range(0, N):
    for j in range(i+1, N):
        if files[i] == files[j]:
            if files[i] not in duplicate:
                duplicate.append(files[i])
filetype = []
for i in duplicate:
    i = i.split(" ")
    filetype.append(i[1])
filetype.sort()
if len(duplicate) > 0:
    for i in filetype:
        print(i)
else:
    print(-1)
