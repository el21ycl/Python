# index operator [] = gives access to a sequence's element (str,list[],tuples())

# you can add a set of square brackets after a string a list or a tuples and
# then list an integer or a range of the elements that you're trying to access

name = "bro Code!"

if(name[0].islower()): #True
    name = name.capitalize()

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(name)

print(first_name)
print(last_name)
print(last_character)





