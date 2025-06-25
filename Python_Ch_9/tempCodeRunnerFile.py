with open("another.txt", "a+") as f:   # used for appending and
    a = f.write("\nThis is a new line added to the file.")  # This will append a new line to the file
    print("Number of characters appended:", a)