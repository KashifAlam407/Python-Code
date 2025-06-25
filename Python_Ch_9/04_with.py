# with open("another.txt", "r") as f:   # used for reading 
#     a = f.read()
with open("another.txt", "w") as f:   # used for writing
    a = f.write("me and you are too good")
print(a)  #why 23 is printedd
# The number 23 is printed because the `write` method returns the number of characters written to the file.
# In this case, the string "me and you are too good" contains 23 characters, including spaces.
# Therefore, when you call `f.write(...)`, it returns 23, which is then printed by the `print(a)` statement.
# This behavior is consistent with the Python documentation for file I/O operations.    





###================================================================
with open("another.txt", "r+") as f:   # used for reading and writing
    a = f.read()
    f.seek(0)  # Move the cursor to the beginning of the file
    f.write("Kashif")

    print("Before writing", a)  # This will print the content of the file
    # f.write("\nThis is a new line added to the file.")  # This will append a new line to the file





###===============================================================
with open("another.txt", "w+") as f:   # used for writing and reading
    a = f.write("Kashif")
    f.seek(0)  # Move the cursor to the beginning of the file
    b = f.read()  # Read the content of the file
    print("Content of the file after writing:", b)  # This will print the content
    print("Number of characters written:", a)  # This will print the number of characters written
# The `w+` mode allows both writing and reading, but it truncates the file to zero length when opened.
# The `r+` mode allows both reading and writing without truncating the file.
# The `seek(0)` method is used to move the file cursor back to the beginning of the file after writing,
# so that the subsequent read operation reads from the start of the file.
# The `read()` method reads the entire content of the file, and the `write()` method writes to the file.
# The `print` statements will show the content of the file and the number of characters written.




###===============================================================
with open("another.txt", "a+") as f:   # used for appending and
    a = f.write("\nThis is a new line added to the file.")  # This will append a new line to the file
    print("Number of characters appended:", a)  # This will print the number of characters appended
    f.seek(0)  # Move the cursor to the beginning of the file
    b = f.read()  # Read the content of the file
    print("Content of the file after appending:", b)  # This will print the content
    print("Number of characters appended:", a)  # This will print the number of characters appended
# The `a+` mode allows both appending and reading. It opens the file for appending, and if the file does not exist, it creates a new one.
# The `seek(0)` method is used to move the file cursor back to the beginning
# of the file after appending, so that the subsequent read operation reads from the start of the file.
# The `read()` method reads the entire content of the file, and the `write()` method appends to the file.
# The `print` statements will show the content of the file and the number of characters appended
# The `a` variable will contain the number of characters appended, which is the length of the string written.
# The `print` statements will show the content of the file and the number of characters appended.
# The `a+` mode is useful when you want to add new content to the end of the file while still being able to read its existing content.

