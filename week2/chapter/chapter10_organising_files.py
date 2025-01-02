import shutil, os
from pathlib import Path

import send2trash

# Copying Files
p = Path.home()
shutil.copy(r"C:\delicious\walnut\waffles\bacon.txt", r'C:\Python-learning\week2\chapter')
shutil.copy(r"C:\delicious\walnut\waffles\bacon.txt", r'C:\Python-learning\week2\chapter\bacon1.txt')

# Copying Folders
shutil.copytree(r"C:\delicious\walnut\waffles", r'C:\Python-learning\week2\chapter\file_orgnaize')

# Moving and Renaming Files and Folders
shutil.move(r"C:\delicious\walnut\waffles\bacon.txt", r'C:\Python-learning\week2\chapter')
shutil.move(r"C:\delicious\walnut\waffles\bacon1.txt", r'C:\Python-learning\week2\chapter\bacon_new.txt')

# Permanently Deleting Files and Folders
# unlink(path) will delete the file at path
os.unlink(r"C:\Python-learning\week2\chapter\bacon.txt")

# rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
os.rmdir(r"C:\Python-learning\week2\chapter\new")
os.unlink(r"C:\delicious\walnut\waffles\New folder")

# shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.
shutil.rmtree(r"C:\Python-learning\week2\chapter\new")

# Safe Deletes with the send2trash Module
baconFile = open(r'C:\Python-learning\week2\chapter\bacon_new.txt', 'a')   # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash(r'C:\Python-learning\week2\chapter\bacon_new.txt')

# Walking a Directory Tree
for folderName, subfolders, filenames in os.walk(r"C:\delicious"):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')

# Compressing Files with the zipfile Module
import zipfile, os

# Reading ZIP Files
exampleZip = zipfile.ZipFile(r"C:\delicious\walnut\waffles\New folder\New folder.zip")
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('baon_.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')
exampleZip.close()

# Extracting from ZIP Files
exampleZip = zipfile.ZipFile(r"C:\delicious\walnut\waffles\New folder\New folder.zip")
exampleZip.extractall()
exampleZip.close()

exampleZip.extract('bacon.txt')

# Creating and Adding to ZIP Files
newZip = zipfile.ZipFile(r"C:\delicious\walnut\waffles\New folder\New.zip", 'w')
newZip.write(r"C:\delicious\walnut\waffles\New folder\baon_.txt", compress_type=zipfile.ZIP_DEFLATED)
newZip.close()



