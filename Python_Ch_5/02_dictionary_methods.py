myDict = {
    "kashif": "Footballer",
    "ashif": "Army boy",
    "aquef": "Engineer",
    "marks": [1,3,4,54],
    "anotherdict": {"kashif": "Coder"},
    1: 3

}

# Dictionary methods
print(myDict.keys())  ## prints the keys of the dictionary
print(type(myDict.keys()))   
print(list(myDict.keys()))  ## you can change it in a list 
print(type(myDict.values()))   
print(list(myDict.values()))
print(myDict.items())   ## prints the (key, value) for all contents of the dictionary
print(myDict)
updateDict = {
    "Lovish": "Friends",
    "Tiger": "Friends",
    "lion": "King",
    "ashif": "Volleyball player"   ## it updates ashif 
}
myDict.update(updateDict)   ## updates the existing list with key value pairs 
print(myDict)

print(myDict.get("kashif"))   ## prints value associated with key "kashif"
print(myDict["kashif"]) 

## The difference between .get and [] bracket syntax in the Dictionaries
print(myDict.get("kashif2"))   ## Return None as kashif2 is not present in the dictionary
# print(myDict["kashif2"])  ## throws an error as kashif2 is not prenest in the dictionary



#---------------------------------
print("\nDictionary Iteration")
d = dict({'x':123, 'y':354})
for i in d:
    # print("%s  %d" % (i, d[i]))   ## here %s and %d is format specifier, %s means it print the value in string type and %d means it print the value in integer type.
    # print(f"{i} : {d[i]}")
    # print(d[i])
    print(i, d[i])




