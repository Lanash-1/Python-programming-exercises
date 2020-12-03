'''

Sample input: 

energy
genuine

Sample output: 

en

'''

firstWord = input().strip()
secondWord = input().strip()
secondWord = secondWord[::-1] 
for i in range(len(firstWord)):
    if firstWord[i] == secondWord[i]:
        print(firstWord[i], end="")
    else:
        break
