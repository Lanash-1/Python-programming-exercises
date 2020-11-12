s1 = input().strip()
s2 = input().strip()
s3 = input().strip()
S = []
S.append(s1)
S.append(s2)
S.append(s3)
word = ""
if ((s1[0] == s2[0]) or (s1[0] == s3[0])) and ((s1[-1] == s2[0]) or (s1[-1] == s3[0])):
    word = s1
elif ((s2[0] == s1[0]) or (s2[0] == s3[0])) and ((s2[-1] == s1[0]) or (s2[-1] == s3[0])):
    word = s2
else:
    word = s3
first = ""
last = ""
for w in S:
    if w != word:
        if word[0] == w[0]:
            first = w
        else:
            last = w
N = len(word) - 2
print(word)
for i in range(1, len(first)):
    print(first[i], end="")
    print("*" * N, end="")
    print(last[i])