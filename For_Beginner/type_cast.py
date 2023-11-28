#type casting = convert the data type of a value to another data type

x = 1   #int
y = 2.0 #float
z = "3" #str

print(y,int(y))
print(y)
y = int(y)
print(y)

print(z*3) # is 333(string)
z = int(z)
print(z*3)

print(x)
x = float(x)
print(x)

print("X is " + str(x))
