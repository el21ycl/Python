import os
# \ blackslash
# need double backslashes because that's the escape sequence for a backslash within a string

# \ escape sequence,用于表示一些特殊的字符或者字符序列,要在字符串中打出\，需要兩個轉義字符
#path = "C:\\Users\\lin\\Documents\\GitHub\\el21ycl\\Workspace\\Python"

# r/R, 讓所有的字符串都是直接按照字面的意思来使用
path = r"C:\Users\lin\Documents\GitHub\el21ycl\Workspace\Python"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location does not exists!")










