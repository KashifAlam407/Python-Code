words = ["donkey", "kaddu", "mote", "dog"]

with open("sample.txt") as f:
    content = f.read()
                                
for word in words:    
    a = content.replace(word, "$@%^&#")
    with open("sample.txt", "w") as f:
        f.write(a)