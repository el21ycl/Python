# \n will go down to a new line
text = "Yoooooooooooooooooo\nThis is some text\nHave a good one!\n"

# it will actually overwrite your current file
with open('test.txt','w') as file:
    file.write(text) 

text1 = 'Append somethings'
# it will actually append some text to your current file
with open('test.txt','a') as file:
    file.write(text1) 










