with open('C:\\Users\\lin\\Documents\\GitHub\\el21ycl\\Workspace\\Python\\test.txt') as file:
    print(file.read()) # This actually close files automatically after openning them

print(file.closed) # to check file closed or not ,if my file is in fact closed this will print true

try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('That file was not found :(')















