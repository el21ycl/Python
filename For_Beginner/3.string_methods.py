
name = "bro code" 
# How long the length of our string
print(len(name)) # 8, including blank space

# How to find a character within a string
print(name.find("o")) # is index 2

# To capitalize that only the first letter 
print(name.capitalize()) # Bro code

# Make your string all uppercase/lowercase
print(name.upper())
print(name.lower())

# isdigit will return True or False, depending on if our string is a digit or not
print(name.isdigit()) # name is a string,so is False, unless name = 123

# isalpha is check to see If your string contains only letters, alphabetical letters
print(name.isalpha()) # if it have space, it is False. When name="Brocode", that is True

# To count how many o's in here
print(name.count("o")) # Bro code has two o, so return two

# Replace all of o to a
print(name.replace("o","a"))

# Print 3 times
print(name*3)
