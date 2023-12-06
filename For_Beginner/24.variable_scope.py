# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created

# Python follow this legb rule, you use any local variables first, then enclosed variables then...
# ... in that order.
# L = Local
# E = Enclosing
# G = Global
# B = Built-in

name = "Bro"   # global scope (available inside & outside functions)

def display_name():
    name = "Code"   # local scope (available only inside this function)
    print(name)
    def display2():
        name = "Lin"
        print(name)

display_name()
print(name)



