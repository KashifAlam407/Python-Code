def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

readFile("01.txt")
readFile("02.txt")
readFile("03.txt")