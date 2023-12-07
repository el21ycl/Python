# Pseudo-random
import random

x = random. randint(1,6) # integer 1~6
print(x)

y = random.random() #0~1
print(y)

mylist = ['rock', 'paper','scissors',5]
z = random.choice(mylist)
print(z)

cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
random.shuffle(cards) # shuffle this list
print(cards)











