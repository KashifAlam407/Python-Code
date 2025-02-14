myDict = {
    "kashif": "Footballer",
    "ashif": "Army boy",
    "aquef": "Engineer",
    "marks": [1,3,4,54],
    "anotherdict": {"kashif": "Coder"}

}

print(myDict["kashif"])
print(myDict["ashif"])
myDict["marks"] = [34, 53, 23, 42]
print(myDict["marks"])   ## dictionary are mutable you can change it
print(myDict["anotherdict"])
print(myDict["anotherdict"]["kashif"])
myDict["kashif"] = "A Coder"
print(myDict["kashif"])   ## dictionary are mutable you can change it


