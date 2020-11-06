No_of_stairs=int(input())  # initialize a vairable to get number of stairs from the user

# initailze a, b, c = 0
a=0   
b=1   
c=1  
for stairs in range(No_of_stairs-1): #  Create a loop till the range No_of_stairs - 1 
    c=a+b  
    a=b
    b=c 
print(c+a)