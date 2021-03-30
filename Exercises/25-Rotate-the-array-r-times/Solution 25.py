rows, cols, r = map(int, input().split())
matrix = []
for i in range(rows):
    matrix.append(list(map(int ,input().split())))

# outer numbers
outer = []
for n in matrix[0]:
    outer.append(n)
    
for i in range(1, rows-1):
    outer.append(matrix[i][cols-1])

for i in range(cols-1,-1,-1):
    outer.append(matrix[-1][i])

for i in range(rows-2,0,-1):
    outer.append(matrix[i][0])

# inner numbers
inner = []
for n in matrix[1][1:cols-1]:
    inner.append(n)

for i in range(2, rows-1):
    inner.append(matrix[i][cols-2])

for i in range(cols-3, 0, -1):
    inner.append(matrix[rows-2][i])
    
for i in range(rows-3, 1, -1):
    inner.append(matrix[i][1])

# rotating outer

o = []
outerlen = len(outer)
if (outerlen > r):
    for i in outer[r:]:
        o.append(i)
    for i in outer[:r]:
        o.append(i)
elif (outerlen == r):
    for i in outer:
        o.append(i)
else:
    for i in outer[r-outerlen:]:
        o.append(i)
    for i in outer[:r-outerlen]:
        o.append(i)

# rotating inner

inn = []
innerlen = len(inner)
if (innerlen > r):
    for i in inner[r:]:
        inn.append(i)
    for i in inner[:r]:
        inn.append(i)
elif (innerlen == r):
    for i in inner:
        inn.append(i)
else:
    for i in inner[r-innerlen:]:
        inn.append(i)
    for i in inner[:r-innerlen]:
        inn.append(i)

# joining the arrays

for i in range(cols):
    print(o[i],end=" ")
print()

leftindex = 0
rightindex = 0
for i in range(1,rows-1):
    print(o[leftindex-1],end=" ")
    print(inn[leftindex-0],end=" ")
    print(inn[rightindex+1], end=" ")
    print(o[rightindex+4])
    leftindex -= 1
    rightindex += 1

for i in range(cols):
    print(o[leftindex-1],end=" ")
    leftindex -= 1

