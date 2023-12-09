import os

source = r'C:\Users\lin\Documents\GitHub\el21ycl\Workspace\Python\test.txt'
destination = r'C:\Users\lin\Desktop\test2.txt'

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination) # that is how to move a file and or directory
        print(source +  " was moved")

except FileExistsError:
    print(source + " was not found")






