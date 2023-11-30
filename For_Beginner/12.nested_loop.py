# nested loop = the "inner loop" will finish all of it's iterations before
#               finishing one iteration of the "outer loop"

rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="") 
        # end="" this will prevent our cursor from moving down to the next line
    print() # print will automatically add a return to the end of the line



