# tuple = collection which is ordered and unchangeable 有順序，不可改的
#         used to group together related data
#       () parentheses
student = ("Bro",21,"male") # if no sperator, default is tuple

print(student)
print(student.count("Bro"))  # 1, how many times a value appears
print(student.index("male")) # 2, it can find the index of a certain value 

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here")

