'''
Check the image for the problem statement and Sample input and output.
'''

N = int(input())                           # N => No of folders/files

files = []                                 # Create a list named files to store the names of the files/folder
for i in range(N):                         # for i in range of N
    files.append(input().strip())          # Append the folder/file name to files list

duplicate = []                             # Create a list named duplicate to store the duplicate files
for i in range(0, N):                      # for i in range of N
    for j in range(i+1, N):                # for j in range of i+1 to N
        if files[i] == files[j]:           # Check whether i'th element in files and j'th element in files are same
            if files[i] not in duplicate:  # Check whether i'th element in files present in duplicate list
                duplicate.append(files[i]) # If not append the element to the duplicate list

filetype = []                              # Create a list named filetype to store the file name of the duplicates
for folder in duplicate:                   # for every folder in duplicate     
    folder = folder.split(" ")             # Split the folder into folder name and file name 
    filetype.append(folder[1])             # Append the file name with type to filetype list

filetype.sort()                            # Sort the file names in the filetype list in ascending order

if len(duplicate) > 0:                     # Check whether the list duplicate has any element
    for file in filetype:                     # if yes, then for each file in filetype list
        print(file)                           # print the file name 
else:                                      # if no
    print(-1)                              # then print -1
