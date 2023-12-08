# copyfile() = copies contents of a file
# copy()  =    copyfile() + permission mode + destination can be a directory
# copy2() =    copy() + copies metadata (file's creation and modification times)

# shutil模块提供了移动、复制、 压缩、解压等操作，恰好与os互补，共同一起使用，基本能完成所有文件的操作
import shutil

shutil.copyfile('test.txt',r'C:\Users\lin\Documents\GitHub\el21ycl\Workspace\Python\copy.txt') 
             # src(source), path dst(destination)
#shutil.copy(,)
#shutil.copy2(,)





