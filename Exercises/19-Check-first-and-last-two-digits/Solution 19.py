'''

Sample input 1: 

155215

Sample output 1: 

yes
.............

Sample input 2: 

9217623

Sample output 2: 

no

'''

Number = input().strip()
if(Number[:2] == Number[-2:]):
    print("yes")
else:
    print("no")