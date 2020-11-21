S = input().strip()
c1, c2 = input().split()
D = []
for i in range(len(S)):
    d = 0
    if S[i] == c1 or S[i] == c2:
        if S[i] == c1:
            for j in range(i+1,len(S)):
                if S[j] != c2:
                    d += 1
                else:
                    D.append(d)
                    break
        else:
            for k in range(i+1, len(S)):
                if S[k] != c1:
                    d += 1
                else:
                    D.append(d)
print(min(D))