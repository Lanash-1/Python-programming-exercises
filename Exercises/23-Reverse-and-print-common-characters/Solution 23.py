'''

Sample input: 

energy
genuine

Sample output: 

en

'''

s1 = input().strip()
s2 = input().strip()
s2 = s2[::-1]
minlen = 0
if(len(s1) < len(s2)):
    minlen = len(s1)
else:
    minlen = len(s2)
for i in range(minlen):
    if s1[i] == s2[i]:
        print(s1[i], end="")
