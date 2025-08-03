# File Handling means, creating,reading,updating or deleting CRUD operations which we can perform on files.

# file = open("helloworld.txt")
# print(file.read())

# file1 = open("superman.txt","w")
file1 = open("superman.txt","a")
file1.write("Hello, This is Arpit and Now I am updating the file")
file1.close()