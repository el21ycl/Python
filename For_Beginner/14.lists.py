# list = used to store multiple items in a single variable
#      []
food = ["pizza","hamburger","hotdog","spaghetti","pudding"]
#         0       1          2        3           4
print(food)
print(food[0])

food[0] = "sushi"

print(food[0])


food.append("ice cream") # append an element to the last one
food.remove("hotdog")
food.pop()   # pop will remove the last element
food.insert(0,"cake")
food.sort()  # this will sort a list alphabetically(a~z)
#food.clear() # it will clear all of the elements of a list


for x in food:
    print(x)

