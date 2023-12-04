#slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step] or (,,)


name = "Bro code"
# index 01234567 positive
# index -8-7-6-5-4-3-2-1 negative

# At this name[0:2], the first index is inclusive, the stopping index is exclusive
#first_name = name[0:2] display 'Br'
first_name = name[:3]

# a shortcut if you leave stop blank, this is a shorthand way of writing
#last_name = name[4:] start to index4 after until the end [0:end]
last_name = name[4:8]
print(first_name,last_name)

# step is how much we are increasing our index between starting and stopping
# normally step is one by default
funky_name = name[0:8:2] #so there are index 0246
#                                            Bocd
# a shorthand way is [::2]

print(funky_name)

reversed_name = name[::-1] # [0:end:-1]
print(reversed_name)

website1 = "http://google.com" # google is [7:13]
#           0123456789
#                       -4321
website2 = "http://wikipedia.com"  # google is [7:16]

slice = slice(7,-4)
print(website1[slice]) # [7:-4], 7 8 9 10 11 12(-5)
print(website2[slice])



