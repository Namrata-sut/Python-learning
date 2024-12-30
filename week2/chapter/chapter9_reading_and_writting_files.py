# Backslash on Windows and Forward Slash on macOS and Linux
from pathlib import Path

print(Path('spam', 'bacon', 'eggs'))
print(str(Path('spam', 'bacon', 'eggs')))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))

# Using the / Operator to Join Paths
print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon/eggs'))
print(Path('spam') / Path('bacon', 'eggs'))

# using join
homeFolder = r'C:\Users\Al'
subFolder = 'spam'
print(homeFolder + '\\' + subFolder)
print('\\'.join([homeFolder, subFolder]))

# Using / math division operator
homeFolder = Path('C:/Users/All')
subFolder = Path('spam')
print(homeFolder / subFolder)
print(str(homeFolder / subFolder))

# The Current Working Directory
print(Path.cwd())

# Change current working directory
import os
print(os.chdir(r'C:\Python-learning\week1\chapter'))
print(Path.cwd())

# The Home Directory
print(Path.home())

# An absolute path, which always begins with the root folder
# A relative path, which is relative to the program’s current working directory

# Creating New Folders Using the os.makedirs() Function
# print(os.makedirs(r'C:\\delicious\\walnut\\waffles'))

# print(Path(r'C:\delicious\spam').mkdir())

# Handling Absolute and Relative Paths
print(Path.cwd().is_absolute())

print(Path('spam/bacon/eggs').is_absolute())
print(Path.cwd() / Path('my/relative/path'))
print(Path.home() / Path('my/relative/path'))

# the absolute path of the argument.
print(os.path.abspath('.'))
print(os.path.abspath(r'.\\Scripts'))

# return True if the argument is an absolute path and False if it is a relative path.
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))

# Getting the Parts of a File Path
p = Path('C:/Users/Al/spam.txt')
print("anchor", p.anchor)
print("parent", p.parent)
print("name", p.name)
print("stem", p.stem)
print("suffix", p.suffix)
print("drive", p.drive)

print(Path.cwd().parents[0])
print(Path.cwd().parents[1])
print(Path.cwd().parents[2])

# dir name and base name
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))
print( os.path.split(calcFilePath))
print(calcFilePath.split(os.sep))
print('/usr/bin'.split(os. sep))

# Finding File Sizes and Folder Contents
print(os.path.getsize("C:\delicious\Context Precision.docx"))
print(os.listdir('C:\delicious'))

totalSize = 0
for filename in os.listdir('C:\delicious'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\delicious',filename))
print(totalSize)

# Modifying a List of Files Using Glob Patterns
p = Path('C:\delicious')
print(p.glob('*'))
print(list(p.glob('*')))

print(list(p.glob('*.txt')))

print(list(p.glob('*.?x?')))
p1 = Path('C:\delicious')
for textFilePathObj in p.glob('*.txt'):
    print(textFilePathObj)  # Prints the Path object as a string.

# Checking Path Validity
winDir = Path('C:\delicious')
notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
calcFile = Path('C:\delicious\Context Precision.docx')
print(winDir.exists())
print(winDir.is_dir())
print(notExistsDir.exists())
print(calcFile.is_file())
print(calcFile.is_dir())

p_write = Path('spam.txt')
p_write.write_text('Hello, world!')
print(p_write.read_text())

# Opening Files with the open() Function
# helloFile = open(Path.home() / 'hello.txt')
helloFile = open('C:\delicious\Context Precision.docx')
print(helloFile)

# Reading the Contents of Files
# helloContent = helloFile.read()
# print(helloContent)

# sonnetFile = open(Path.home() / 'sonnet29.txt')
# sonnetFile.readlines()

# Writing to Files
baconFile = open(r'C:\delicious\walnut\waffles\bacon.txt', 'w')
baconFile.write('Hello, world!\n')
# content = baconFile.read()
# baconFile.close()
# print(content)
with open(r'C:\delicious\walnut\waffles\bacon.txt') as baconFile:
    content = baconFile.read()
print(content)

# Saving Variables with the shelve Module
# import shelve
# shelfFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()

