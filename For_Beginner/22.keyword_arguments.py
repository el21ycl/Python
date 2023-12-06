# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives


def hello(first,middle,last):
    print("hello "+first+" "+middle+" "+last)

hello("Bro","Dude","Code")

# use keyword arguments, we need to each argument with a unique identifier 
# and that identifier is the name of the parameter we want to associate each argument with
hello(last="Code",middle="Dude",first="Bro")
#     ^identifier





