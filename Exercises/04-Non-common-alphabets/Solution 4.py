'''
Sample Input:
apple
mango

Sample Output:

mngople


'''

s1 = input().strip()     
s2 = input().strip()
l1 = []
l2 = []

for i in s1:           # for each alphabet in s1 
    l1.append(i)       # append to the list l1

for i in s2:           # for each alphabet in s2
    l2.append(i)       # append to the list l2

result = []

for ch in l2:                      # for every element in the list l2
    if ch not in l1:               # if the element is not in list l1
        if ch not in result:       # And if the element is not already in  result
            result.append(ch)      # Then append that element to result

for ch in l1:                      # for every element in the list l1
    if ch not in l2:               # if the element is not in lsit 2
        if ch not in result:       # And if the element is not alreadt in the result
            result.append(ch)      # Then append that element to result

for ch in result:                  # for every element in the result
    print(ch, end="")              # print the element with end = ""
