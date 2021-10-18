# This is a program to accept a filename and print the extension of that.
filename=input("enter the file name: ")
f_extns=filename.split(".")
print("the extension of the file is: " + repr(f_extns[-1]))
