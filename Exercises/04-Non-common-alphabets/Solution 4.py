'''
Sample Input:
apple
mango

Sample Output:

mngople


'''

s1 = input().strip()
s2 = input().strip()
result = ""
for ch in s2:
    if ch not in s1:
        if ch not in result:
            result = result + ch
for ch in s1:
    if ch not in s2:
        if ch not in result:
            result = result + ch
print(result)
