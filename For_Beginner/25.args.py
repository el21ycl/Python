# *args(name) = parameter that will pack all arguments into a tuple
#               useful so that a function can accept a varying amount of arguments
# *asterisk

'''
def add(num1,num2):
    sum = num1+num2
    retuen sum

print(add(1,2))
'''
# if print(add(1,2,3))
# use args parameter so what we're going to do is replace all of our parameters with asterisk args
def add(*stuff):
    sum = 0
    stuff = list(stuff) # cast our tuple as a list, because tuples are unchangeable
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))


