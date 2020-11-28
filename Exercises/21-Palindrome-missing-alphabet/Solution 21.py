'''

Sample input: 

malayaam

Sample output: 

l

'''

S = input().strip()
N = len(S) - 1
missing = ""
for i in range(len(S)):
    if S[i] != S[N-i]:
        if i == N-i-1:
            missing = S[i]
            break
        elif S[i] == S[N-i-1]:
            missing = S[N-i]
            break
        elif S[i+1] == S[N-i]:
            missing = S[i]
            break
print(missing
