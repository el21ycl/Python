# str.format() = optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item)

# a more elegant way, they work in order the first format field will insert the first value
print("The {} jumped over the {}".format("cow","moon"))
#          ^ curly braces, format field
print("The {} jumped over the {}".format(animal,item))
#                                        index 0, index 1
print("The {1} jumped over the {0}".format(animal,item))  # positional argument

print("The {item} jumped over the {animal}".format(animal = "cow",item = "moon")) # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal,item))

#--------------------------------------------------------
name = "Bro"
print("Hello, my name is {}".format(name))
# : colon
# add some padding {positional/keyword/void: }
#                        to allocate 10 spaces worth of room
print("Hello, my name is {:10}. Nice to meet you".format(name))
# to left align, with a less than sign
print("Hello, my name is {:<10}. Nice to meet you".format(name))
# to right align, with a greater than sign
print("Hello, my name is {:>10}. Nice to meet you".format(name))
# to center align, with a carrot
print("Hello, my name is {:^10}. Nice to meet you".format(name))

#--------------------------------------------------------

number1 = 1003.14159
number2 = 1000
#                         floating point number
print("The number is {:.2f}".format(number1)) # .2f, 3.14/ .3f, 3.142
# it will automatically add a comma to all 1000s places
print("The number is {:,}".format(number1))
# This will display a binary representation of your number
print("The number is {:b}".format(number2))
# This will display an octal representation of your number
print("The number is {:o}".format(number2))
# This will display a hexadecimal lowercase x/uppercase X representation of your number
print("The number is {:x}".format(number2))
print("The number is {:X}".format(number2))
# This will display a scientific notation representation of your number
print("The number is {:.2e}".format(number2)) # exponential, 1.00e+03
print("The number is {:E}".format(number2))

