print ("hello world!")

#Printing Quotes
print ('Hello, "world!"')
print ("Hello, 'World!'")

#New Line print
print("My name is\nbot")

#Writing in multiple lines
print("""
-------
|     |
-------
""")

#multiple Arguments to print function
print("My", "name", "is", "bot")

#Adding a separator
print("My", "name", "is", "bot", sep="_")

#Telling how to end a line
print("My", "name", "is", end="") #Will remove \n characters
print("bot")

#Using both sep and end
print("Hello", "My name is", sep=".", end=" ") #separates each parameter with . and brings next print to old line
print("bot", end=".")

print()
