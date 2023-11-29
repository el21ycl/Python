# input() is always input string data type
name = input("What your name is: ")

age = int(input("How old are you: "))
age = age + 1
height = float(input("How tall are you: "))

print("Hello " + name)
print("You are " + str(age) + " years old")
print("You are " + str(height) + " cm tall")