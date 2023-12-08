# exception = event detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    #print(result)

# When denominator = 0, will display ZeroDivisionError
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")

# When denominator = string, will display ZeroDivisionError
except ValueError as e:
    print(e)
    print("Enter only number plz")

# this accept exception block will catch all sorts of different exceptions
except Exception as e: # as e can display what exception occurred too as well
    print(e)  # this is an additional way in which you cloud handle an exception although it's 
              # entirely optional
    print("somthing went wrong :(")                    

else:
    print(result)

# whether or not we catch an exception we will always execute any code that is within 
# the block of code for our finale clause
finally:
    print("This will alwaus execute")





