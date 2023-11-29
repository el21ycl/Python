# for loop = a statement that will execute it's a block of code
#            a limit amount of times
#
#            while loop = unlimited 
#     it could iterate an unlimited or infinite amount of times depending on condition
#            for loop = limited
#     it will only iterate an limited amount of times and before we start executing its block of code
#     we already know how many times we're going to repeat this block of code

import time # it will be waiting one second after each iteration

'''
for i in range(10): # 0~9
    print(i)

for j in range(50,100,2): # 50~99, the interval is 2
    print(j)

for m in "Bro code": # print each letter, including blank
    print(m)
'''

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1) # wait 1 second
print("Happy New year")
