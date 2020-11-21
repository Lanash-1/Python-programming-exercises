'''

Sample input: 

spaceship
c s

Sample output: 

1

'''
S = input().strip()  # Get the input string from the user and store it in a variable
c1, c2 = input().split()   # c1 , c2 stores the alphabets for which we need to find the minimum distance
D = []        # create a empty array D to store the values of distance

for i in range(len(S)):   # for i in range from 0 to length of the input string
    d = 0                 # create a variable and assign its value to 0
    if S[i] == c1 or S[i] == c2:    # check whether ith character of S and c1 are equal or ith character of S and c2 are equal
        if S[i] == c1:          # if ith character of S and c1 are equal
            for j in range(i+1,len(S)):    # for j in range from i+1 to length of S
                if S[j] != c2:                  # check if jth character of S and c2 are not equal
                    d += 1                          # increase the value of d by 1
                else:                           # else
                    D.append(d)                     # append the value of d to the array D
                    break                           # break from the loop
        else:                   # else
            for k in range(i+1, len(S)):   # for k in range from i+1 to length of S
                if S[k] != c1:                  # check whether the kth character of S and c1 are not equal
                    d += 1                          # then increase the value od d by 1
                else:                           # else
                    D.append(d)                 # append the value of d to the array D

print(min(D))      # print the minimum value from the array D