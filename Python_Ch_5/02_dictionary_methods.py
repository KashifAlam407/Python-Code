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
print(myDict.get("kashif2", "Not Found"))  ## Returns "Not Found" if key is not present
print(myDict["kashif2"] if "kashif2" in myDict else "Not Found")  ## Returns "Not Found" if key is not present

d1 = {num: ("even" if num % 2 == 0 else "odd") for num in range(10)}  ## creates a dictionary with numbers from 0 to 9 as keys and "even" or "odd" as values
print(d1)  ## prints the dictionary created using dictionary comprehension


#---------------------------------
dict5 = {'Alice': 1000, 'Bob': 1500, 'Charlie': 800, 'Diana': 1200}  ## creates a dictionary with names as keys and salaries as values
dictionary = {name: (0.2*salary if salary > 1000 else 0.1*salary) for name, salary in
              dict5.items()}## creates a dictionary with names as keys and bonus as values based on the salary
print(dictionary)  ## prints the dictionary with names and their respective bonuses


#---------------------------------
print("\nDictionary Creation")
dict1 = {'Alice': 10, 'Kashif': 45, 'Niraj': 50, 'Bob': 20, 'Charlie': 30}  ## creates a dictionary with key-value pairs
print(dict1)  ## prints the dictionary created using curly braces

dict5 = dict(Alice=10, Kashif=45, Niraj=50, Bob=20, Charlie=30)  ## creates a dictionary using the dict constructor
print(dict5)  ## prints the dictionary created using the dict constructor
print(dict5['Alice'])  ## prints the value associated with the key 'Alice'
print(dict5.get('Alice'))  ## prints the value associated with the key 'Alice' using the get method
print(dict5.get('Alice', 'Not Found'))  ## prints the value associated with the key 'Alice' or 'Not Found' if key is not present
print(dict5.get('Unknown', 'Not Found'))  ## prints 'Not Found' as 'Unknown' key is not present in the dictionary


#---------------------------------
print("\nDictionary Iteration")
d = dict({'x':123, 'y':354})
for i in d:
    # print("%s  %d" % (i, d[i]))   ## here %s and %d is format specifier, %s means it print the value in string type and %d means it print the value in integer type.
    # print(f"{i} : {d[i]}")
    # print(d[i])
    print(i, d[i])

d1 = dict{'name': 'kashif', 'age': 20, 'city': 'Karachi'}
for key, value in d1.items():
    print(f"{key} : {value}")  ## prints the key and value of the dictionary
    # print(key, value)  ## prints the key and value of the dictionary
    # print(d1[key])  ## prints the value associated with the key
    # print(d1.get(key))  ## prints the value associated with the key   

#---------------------------------
print("\nDictionary Comprehension")
d2 = {i: i**2 for i in range(10)}  ## creates a dictionary with keys as numbers from 0 to 9 and values as their squares
print(d2)
d3 = {i: i**2 for i in range(10) if i % 2 == 0}  ## creates a dictionary with keys as even numbers from 0 to 9 and values as their squares
print(d3)


#---------------------------------
print("\nDictionary Merging")
d4 = {'a': 1, 'b': 2}
d5 = {'c': 3, 'd': 4}
d6 = {**d4, **d5}  ## Merging two dictionaries using unpacking
print(d6)  ## prints the merged dictionary
d7 = d4 | d5  ## Merging two dictionaries using the | operator (Python 3.9+)
print(d7)  ## prints the merged dictionary
d8 = d4.copy()  ## Creates a shallow copy of d4
d8.update(d5)  ## Merges d5 into the copy of d4
print(d8)  ## prints the merged dictionary



#---------------------------------
print("\nDictionary Sorting")
d9 = {'b': 2, 'a': 1, 'c': 3}
sorted_keys = sorted(d9.keys())  ## Sorts the keys of the dictionary
print(sorted_keys)  ## prints the sorted keys
sorted_dict = {k: d9[k] for k in sorted_keys}  ## Creates a new dictionary with sorted keys
print(sorted_dict)  ## prints the sorted dictionary
sorted_items = sorted(d9.items(), key=lambda item: item[1])  ## Sorts the items of the dictionary by value
print(sorted_items)  ## prints the sorted items
#---------------------------------
print("\nDictionary Filtering")
d10 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = {k: v for k, v in d10.items() if v > 2}  ## Filters the dictionary to include only items with values greater than 2
print(filtered_dict)  ## prints the filtered dictionary
#---------------------------------
print("\nDictionary Length")
d11 = {'a': 1, 'b': 2, 'c': 3}
print(len(d11))  ## prints the length of the dictionary (number of key-value pairs)
#---------------------------------
print("\nDictionary Copying")
d12 = {'a': 1, 'b': 2, 'c': 3}
d13 = d12.copy()  ## Creates a shallow copy of the dictionary
print(d13)  ## prints the copied dictionary
d14 = dict(d12)  ## Creates a new dictionary from the existing one
print(d14)  ## prints the new dictionary created from the existing one
#---------------------------------
print("\nDictionary Clearing")
d15 = {'a': 1, 'b': 2, 'c': 3}
d15.clear()  ## Clears all items from the dictionary
print(d15)  ## prints the cleared dictionary (should be empty)
#---------------------------------
print("\nDictionary Setdefault")
d16 = {'a': 1, 'b': 2}
print(d16.setdefault('c', 3))  ## Sets 'c' to 3 if it doesn't exist, returns 3
print(d16)  ## prints the dictionary after setdefault
print(d16.setdefault('a', 5))  ## Returns the value of 'a' (1), does not change it
print(d16)  ## prints the dictionary after setdefault (should remain unchanged)
#---------------------------------
print("\nDictionary Pop")



