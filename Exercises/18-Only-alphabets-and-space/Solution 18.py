'''

Sample input: 

Hello  # @ World

Sample output: 

Hello    World

'''
String = input().strip()
for character in String:
    if(character.isalpha()) or (character == " "):
        print(character,end="")