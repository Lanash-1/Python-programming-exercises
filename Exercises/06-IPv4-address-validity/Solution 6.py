'''
The program need to check whether the given IPv4 address in valid or Invalid

Sample input 1:

127.3.5.0

Sample output 1:

Valid

Sample input 2:

257.0.0.1

Sample output 2:

Invalid
'''

ip = list(map(str, input().split(".")))   # Get the IPv4 address and split it into list separating with '.'

count = 0                                 # Declare a varaible count and assign it's value to 0

for i in ip:                              # for every element in the ip list
    if i == "":                           # if the element is none character
        count += 1                        # increase the value of count by 1
    elif int(i) < 0 or int(i) > 255:      # Or if the element is less than 0 and greater than 255
        count += 1                        # increase the value of count by 1

if count > 0 or len(ip) != 4:             # if the value of count is greater than 0 or length of ip is not equal to 4
    print("Invalid")                      # then print Invalid
else:                                     # Else
    print("Valid")                        # print Valid