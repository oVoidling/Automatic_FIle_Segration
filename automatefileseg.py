import os
import shutil

source = "C:/Users/HP/Downloads"
destination = "C:/Users/HP/Desktop"

list_of_files = os.listdir(source)
print(list_of_files)
extentionsdoc = [".txt",".doc",".docx",".pdf"]
extentionspic = [".jpg",".jpeg",".PNG",".gif"]

for i in list_of_files:
    root,extention = os.path.splitext(i)
    if(extention == " "):
        continue
    elif(extention in extentionsdoc):
        path1 = source + "/" + i
        path2 = destination + "/" + "Document_files"
        path3 = destination + "/" + "Document_files" + "/" + i
        if(os.path.exists(path2)):
            print("Moving " + i + ".......")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + i + ".......")
            shutil.move(path1,path3)
    else:
        continue
        

for i in list_of_files:
    root,extention = os.path.splitext(i)
    if(extention == " "):
        continue
    elif(extention in extentionsdoc):
        path1 = source + "/" + i
        path2 = destination + "/" + "Image_files"
        path3 = destination + "/" + "Image_files" + "/" + i
        if(os.path.exists(path2)):
            print("Moving " + i + ".......")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + i + ".......")
            shutil.move(path1,path3)
    else:
        continue