'''
Check the image given for the problem statement and the sample input and output.
'''

S = list(map(str, input().split()))    # Create a list S and store the given input by converting it into a list
result = []                            # create a list named result to store the output

for i in range(len(S)-1):              # for i in range of lenght of S-1
    if (S[i])[-1] == (S[i+1])[0]:      # if the -1st character of the ith element in the list is equal to 0th character of the i+1th element in the list
        result.append(S[i+1])          # then add i+1th element of the list S to the list result

if len(result) > 0:                    # if no of element in the list result is greater than zero
    for word in result:                # then, for every word in the list result
        print(word, end=" ")           # print the word and end with a space
else:                                  # else
    print(-1)                          # print -1
