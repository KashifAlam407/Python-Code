myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}

print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
print("The mmeaning of your word is:" , myDict[a])  ## throws an error if the word is not present in the dictionary 

## Below line does not throws an error if key is not present in the dictionary, prints None
print("The mmeaning of your word is:" , myDict.get(a))
