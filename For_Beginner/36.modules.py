# module = a file containing python code. May contain function, classes, etc.
# used with modular programming, which is to separate a program into parts

# import the nmae of the module
'''
import function
function.hello()
function.bye()
'''
import function as fun # as, and what sort of nickname should we give function

fun.hello()
fun.bye()

#全都导入到当前的命名空间
from function import *
hello()
bye()

# 导入一个指定的部分到当前命名空间中
from function import hello,bye
hello()
bye()

# this will populate a listing of all modules available
# help("modules")




