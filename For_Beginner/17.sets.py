# set = collection which is unordered, unindexed. No duplicate values
#       {} curly braces

utensils = {"fork","spoon","knife","knife","knife"}
print(utensils)

dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
'''
for x in utensils:
    print(x)

dishes.update(utensils)
for y in dishes:
    print(y)
'''
#dinner_table = utensils.union(dishes)
dinner_table = utensils | dishes
for x in dinner_table:
    print(x)

print(utensils.difference(dishes)) # what is utensils has that dishes doesn't
print(utensils.intersection(dishes)) # it will return whatever element that they have in common
