'''

Sample input:

3
Ram 45 65 45
Geetha 60 30 50
Soundarya 80 90 80

Sample output: 

Ram
Soundarya

'''

noOfStudents = int(input())
info = []
for i in range(noOfStudents):
    info.append(list(map(str, input().strip().split())))
names = []
for i in range(noOfStudents):
    names.append((info[i])[0])
marks = []
for i in info:
    marks.append(i[1:])
result = []
for i in range(noOfStudents):
    total = 0
    average = 0
    for m in marks[i]:
        total = total + int(m)
    average = total//3
    if average>=40 and total>=150:
        result.append(names[i])
result.sort()
for i in result:
    print(i)