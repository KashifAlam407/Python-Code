greeting = "Good Morning, "
name = "Kashif"
# print(type(name))
c = greeting + name
print(c)
print(name[3])  # gives the index of the name variable
# name[3] = "dgf" # does not work
print(name[0:4])  # string slicing
print(name[:4])
print(name[0:])
print(name[0:-1])
print(name[-1])
print(name[-6:-1])   ## here index -6 is equal to index 0
print(name[-6:])
print(name[-6:6])

## string slicing with skip value
name = "kashifIsAGoodBoy"
print(name[0:12:1])  ## it does not skip the value
print(name[0:12:2])   ## it skip 1 value
print(name[0::2])



###=======================
s = "Hello World!"
s = s[::-1]
print(s)

for k in range(len(s)):
    x = s.find(" ")
    for i in range(x+1):
        print(s[x-i], end="")
    k = k+x

###=========================
sentence = "Hello World!"
reversed_words = ' '.join(sentence.split()[::-1])
print(reversed_words)

####-===========================
s = "Hello World!"
word = s.split()  # This splits the string into a list of words
print(s.split()) # This will split the string into a list of words
reversed_words = word[::-1] # This reverses the entire string
print(" ".join(reversed_words))

s = "Hello World!"
k = " ".join(s.split()[::-1])
print(k)


s1 = k[0]
s2 = k[1]
print(s1 + " " + s2)

####===========================
# Reversing a list in Python
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr[::-1])  # This will reverse the

# arr = arr.reverse() ### Error this line will not work because reverse() returns None
# list in place, but does not return a new list

arr.reverse() 
print(arr)  # This will reverse the list in place



###===============================
s3 = "1234Kashif5688Alam"
s4 = "kashifalam843567389654567"
print(s3.isdigit())  # This will return False because the string contains letters
print(s3.isalpha())  # False, because it contains numbers
print(s3.isalnum())  # True, because it contains both letters and numbers
print(s3.islower())  # False, because it contains uppercase letters
print(s4.islower())  # True, because it contains only lowercase letters
print(s3.isupper())  # False, because it contains lowercase letters
print(s3.isspace())  # False, because it contains non-space characters
print(s3.startswith("1234"))  # True, because the string starts with "1234"
print(s3.endswith("Alam"))  # True, because the string ends with "Alam"
print(s3.capitalize())  # "1234kashif5688alam" - capitalizes the first character
print(s3.title())  # "1234Kashif5688Alam" - capitalizes the first character of each word
print(s4.title())  # "Kashifalam843567389654567" - capitalizes the first character of each word in a lowercase string
print(s3.lower())  # "1234kashif5688alam" - converts all characters to lowercase
print(s3.upper())  # "1234KASHIF5688ALAM" - converts all characters to uppercase
print(s3.swapcase())  # "1234kASHIF5688aLAM" - swaps the case of all characters
print(s3.replace("Kashif", "Ali"))  # "1234Ali5688Alam" - replaces "Kashif" with "Ali"
print(s3.split("Kashif"))  # ['1234', '5688Alam'] - splits the string at "Kashif"
print(s3.count("Kashif"))  # 1 - counts occurrences of "Kashif"
print(s3.find("Kashif"))  # 4 - finds the index of "Kashif" in the string
print(s3.index("Kashif"))  # 4 - finds the index of "Kashif" in the string, raises ValueError if not found
print(s3.strip("1234"))  # "Kashif5688Alam" - removes leading and trailing "1234"
print(s3.lstrip("1234"))  # "Kashif5688Alam" - removes leading "1234"
print(s3.rstrip("Alam"))  # "1234Kashif5688" - removes trailing "Alam"
print(s3.zfill(20))  # "0000001234Kashif5688Alam" - pads the string with zeros to make it 20 characters long
print(s3.center(30, '*'))  # "*******1234Kashif5688Alam*******" - centers the string in a field of 30 characters, padding with '*'
print(s3.ljust(30, '*'))  # "1234Kashif5688Alam***************" - left-justifies the string in a field of 30 characters, padding with '*'
print(s3.rjust(30, '*'))  # "***************1234Kashif5688Alam" - right-justifies the string in a field of 30 characters, padding with '*'
print(s3.partition("Kashif"))  # ('1234', 'Kashif', '5688Alam') - splits the string into a tuple at the first occurrence of "Kashif"
print(s3.rpartition("Kashif"))  # ('1234', 'Kashif', '5688Alam') - splits the string into a tuple at the last occurrence of "Kashif"
print(s3.splitlines())  # ['1234Kashif5688Alam'] - splits the string into a list of lines (not applicable here as there are no newlines)
print(s3.join(["Hello", "World"]))  # "Hello1234Kashif5688AlamWorld" - joins the list with the string as a separator
print(s3.startswith("1234"))  # True, checks if the string starts with "1234"
print(s3.endswith("Alam"))  # True, checks if the string ends with "Alam"
print(s3.isnumeric())  # False, because it contains letters
print(s3.isdecimal())  # False, because it contains letters
print(s3.isidentifier())  # False, because it contains numbers and is not a valid identifier
print(s3.casefold())  # "1234kashif5688alam" - case-insensitive version of lower()
print(s3.format("Kashif"))  # "1234Kashif5688Alam" - formats the string with "Kashif"
print(s3.format_map({"name": "Kashif"}))  # "1234Kashif5688Alam" - formats the string with a dictionary
print(s3.translate(str.maketrans("1234", "5678")))  # "5678Kashif5688Alam" - translates characters '1', '2', '3', '4' to '5', '6', '7', '8'
print(s3.removeprefix("1234"))  # "Kashif5688Alam" - removes the prefix "1234"  
print(s3.removesuffix("Alam"))  # "1234Kashif5688" - removes the suffix "Alam"
print(s3.casefold())  # "1234kashif5688alam" - case-insensitive version of lower()
print(s3.format("Kashif"))  # "1234Kashif5688Alam" - formats the string with "Kashif"
print(s3.format_map({"name": "Kashif"}))  # "1234Kashif5688Alam" - formats the string with a dictionary
print(s3.translate(str.maketrans("1234", "5678")))  # "5678Kashif5688Alam" - translates characters '1', '2', '3', '4' to '5', '6', '7', '8'
print(s3.removeprefix("1234"))  # "Kashif5688Alam" - removes the prefix "1234"
print(s3.removesuffix("Alam"))  # "1234Kashif5688" - removes the suffix "Alam"