letter = '''Dear <|NAME|>,
Greeting from ABC coding house. I am happy to tell you about selection
You are selected!
Have a great day ahead!
Thanks and ragards,
Bill
Date: <|DATE|>
'''
name = input("Enter your name: ")
date = input("Enter Date: ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print()  ## it prints a gap (blank line) between user input and letter
print(letter)

# print(letter.replace("<|NAME|>", name) + letter.replace("<|DATE|>", date))
