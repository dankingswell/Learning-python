# writing to text files  

#error
#open("fakename.txt")

file =  open("exampleText.txt")

##prints entire file as string
#print(file.read())

#resets file to location, file will read from end if read before
#print(file.read() +  "See nothing")
file.seek(0)
#print(file.read() + " Read from the start")


# returns lines of text file with line breaks as list 
file.seek(0)
#print(file.readlines())
##print 2nd line
file.seek(0)
#print(file.readlines()[1])
file.close()

# file paths, for windows use \ starting with \\ for c:\\
# for mac and linux use /
# will open as .py if no filename given eg "Python" will open as Python.py

myfile = open("./Folder/textinfile.txt")
lines = myfile.readlines()
#print(lines)
# close document to close stream
myfile.close()


#best practice with works as a function and must include :
with open("./Folder/textinfile.txt") as Fileinfolder:
    lines = Fileinfolder.read()
    #print(lines)

# mode for opening file, by default read  (mode R )can be adjusted by changing mode
newFile = open("./Folder/neworoveride.txt",mode="w") # or you can have parameters as (fielname, "W" or "R" Etc)
newFile.write("Hello world i'm being written too and being overridden, i'll make a new file if i don't exist though")
newFile.close()

# "r+" for reading a writing 
with open("./Folder/neworoveride.txt","r") as written_file:
    #print(written_file.readlines())
    x=1


# append to a file == "a", append or read "a+"

appendedfile = open("exampleText.txt","a+")
appendedfile.write(" this line has been appended ")
appendedfile.seek(0)
print(appendedfile.read())
appendedfile.close()