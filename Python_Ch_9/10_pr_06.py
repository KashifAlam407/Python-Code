with open("log.txt") as f:
    content = f.read()  # you can also use lower() after f.read()

if "python" in content.lower():
    print("yes python is present")
else:
    print("No python is not present")
    