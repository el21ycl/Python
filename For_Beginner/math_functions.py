# A bunch of these functions located within the math module
import math

pi = 3.14
p = 2.84
x = 1
y = 2
z = 3

# round() is a built-in function, it will be rounded to the nearest whole integer 近似值
print(round(pi))
print(round(p))

# it will round a number up/down to the nearest whole integer
print(math.ceil(pi))  # 3.14 rounded up is 4
print(math.floor(pi)) # 3.14 rounded down is 3

# abs() will give you the absolute value of a number 絕對值
print(abs(pi))

# pow() will raise a base number to a power 指數
print(pow(pi,2))

# sqrt() is a square root 根號
print(math.sqrt(220))
print(sqrt(22))

# max() will find the largest/smallest of these values 
print(max(x,y,z))
print(min(x,y,z))



