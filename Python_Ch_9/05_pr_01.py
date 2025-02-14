## to test whether twinkle is present in the 'poems.txt' or not

f = open("poems.txt")
p = f.read()
# if "twinkle" in p:
if "twinkle" in f.read():
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()