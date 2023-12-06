# dictionary = A changeable, unordered collection of unique key: value pairs
#              Fast because they are use hashing, allow to access a value quickly
# d = {key1 : value1, key2 : value2 }     
#      (int,str,tuples)    
#1. 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
#2. 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行    
#            keys:values
capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}

capitals.update({"Taiwan":"Taipei"})
capitals.update({"USA":"Las Vegas"}) # cover Washington DC
capitals.pop('China')

# print(capitals['Russia']) this isn't always safe, if print(['Germany']),it will error
#                ^把相应的键放入熟悉的方括弧 square bracket

print(capitals.get('Germany')) # it will print none

print(capitals.keys())

print(capitals.values())

print(capitals.items())

for key,value in capitals.items():
    print(key,value)
    
#capitals.clear()
