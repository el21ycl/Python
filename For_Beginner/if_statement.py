# if statement = a block of code that will execute if it's condition is True

age = int(input("How old are you: "))

if age >= 18:      # first check
    print("You are an adult!") #if you input 100, it will display adult because it first judged it >=18
                               #and then skip  everything
elif age == 100:
    print("You are a century old")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You are a child!")

'''
if age == 100:      
    print("You are a century old")                              
elif age >=18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You are a child!")
'''