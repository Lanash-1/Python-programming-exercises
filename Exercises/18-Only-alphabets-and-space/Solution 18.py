S = input().strip()
for ch in S:
    if(ch.isalpha()) or (ch == " "):
        print(ch,end="")