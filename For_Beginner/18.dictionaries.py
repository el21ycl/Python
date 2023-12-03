# dictionary = A changeable, unordered collection of unique key: value pairs
#              Fast because they are use hashing, allow to access a value quickly
# d = {key1 : value1, key2 : value2 }     
        
#            keys:values
capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}

capitals.update({"Taiwan":"Taipei"})
capitals.update({"USA":"Las Vegas"}) # cover Washington DC
capitals.pop('China')

print(capitals('Russia')) # his isn't always safe, if print(['Germany']),it will error

print(capitals.get('Germany')) # it will print none

print(capitals.keys())

print(capitals.values())

print(capitals.items())

for key,value in capitals.items():
    print(key,value)
    
capitals.clear()
