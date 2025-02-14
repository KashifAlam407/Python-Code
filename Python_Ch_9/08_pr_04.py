with open("sample.txt") as f:
    content = f.read()
a = content.replace("donkey", "$@%^&#")
with open("sample.txt", "w") as f:
    f.write(a)