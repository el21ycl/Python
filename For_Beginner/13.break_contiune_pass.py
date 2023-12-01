# loop control statement = change a loops execution from its normal sequence

# break =     used to terminate the loop entirely
# continue =  skips to the next iteration of the loop
# pass =      does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
       break

phone_number = "123-456-789"

for i in phone_number:
    if i =="-":
        continue    # it skips to the next iteration of the loop
    print(i,end="")

for j in range(1,21): # 1~20
    if j == 13:
        pass
    else:
        print(j)


