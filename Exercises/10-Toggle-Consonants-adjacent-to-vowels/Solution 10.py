'''

Sample input:

adjAcENt

Sample output:

aDJACEnt


'''

S = input().strip()
Slist = []
for ch in S:
    Slist.append(ch)
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
N = len(S)
for i in range(N):
    if i == 0:
        if Slist[i] not in vowels:
            if Slist[i+1] in vowels:
                if Slist[i].isupper():
                    Slist[i] = S[i].lower()
                else:
                    Slist[i] = S[i].upper()
    elif i == N-1:
        if Slist[i] not in vowels:
            if Slist[i-1] in vowels:
                if Slist[i].isupper():
                    Slist[i] = S[i].lower()
                else:
                    Slist[i] = S[i].upper()
    else:
        if Slist[i] not in vowels:
            if Slist[i+1] in vowels or Slist[i-1] in vowels:
                if Slist[i].isupper():
                    Slist[i] = S[i].lower()
                else:
                    Slist[i] = S[i].upper()
for ch in Slist:
    print(ch, end="")
