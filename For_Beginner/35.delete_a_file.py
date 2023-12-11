import os
import shutil

path = 'C:\\Users\\lin\\Desktop\\test'

try:
#    os.remove(path) # delete a file 如果这个路径是一个文件夹，则会抛出OSError的错误，这时需用用rmdir()来删除
#    os.rmdir(path)  # to delete an empty folder(directory) there is a different function
     shutil.rmtree(path) # delete a directory文件夾 containing files文件
except FileExistsError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError as e:
    print(e)
    print("You can not delete that using that function")
else:
    print(path + " was deleted")












