#Four data type are in here
# that is a string data type
print('Hello, world') 

name =  "Ethan"
name_last = "Lin"
name_full = name+" "+name_last
print('Hello' + name)
print("Hi"+" "+name+" "+name_last)
print(name_full)

#number is int(integer) data type
age = 21 
age = age + 1 # age += 1
print(age)
#If you need to display a variable of a different data type along with the string, 
#you would need to use a stringcast to convert that data type
print('Your age is '+ str(age))

#Float data type
height = 250.5 
print("Your height is: "+ str(height) + "cm")

#Bool data type is only True/False
human = False 
print("Are you a human: " + str(human))
#type()will tell you what is that data type
print(type(name),type(age),type(height),type(human))

