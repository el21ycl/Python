# **kwargs(name) = parameter that will pack all arguments into a dictionary{}
#            useful so that a function can accept a varying amount of keyword arguments
'''
def hello(first,last):
    print("Hello "+first+" "+last)

hello(first="Bro",last="Code")
'''

# use two asterisk then quarks
def hello(**names):
    #print("Hello "+ names["first"]+" "+ names['last'])
    print("Hello",end=" ")
    for key,value in names.items():
        print(value,end=" ")
    print()

hello(first="Bro",middle = "Dude",last="Code")
hello(title = "Mr",first="Bro",middle = "Dude",last="Code")




