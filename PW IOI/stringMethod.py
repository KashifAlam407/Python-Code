### Using .format() method
# The .format() method is used to format strings in Python. It allows you to insert values into a string by using curly braces {} as placeholders.
# The values to be inserted are passed as arguments to the .format() method. This method is useful for creating dynamic strings where the values can change based on user input or other factors.

name = "John"
age = 30
city = "New York"

print("My name is {}, I am {} years old and I live in {}".format(name, age, city))
print("My name is {0}, I am {1} years old and I live in {2}".format(name, age, city))  # using indexing
print("My name is {name}, I am {age} years old and I live in {city}".format(name=name, age=age, city=city))  # using keyword arguments 

print(f"My name is {name}, I am {age} years old and I live in {city}")  # using f-strings (Python 3.6+)
print("My name is %s, I am %d years old and I live in %s" % (name, age, city))  # using old-style string formatting



print("Name", name, "Age", age, "City", city)  # using comma to separate values
# print("Name" + name + "Age" + age + "City" + city)  # using + to concatenate strings
print("Name" + str(name) + "Age" + str(age) + "City" + str(city))  # using str() to convert values to strings
print("Name:", "Kashif", "Age:", 20, "City:", "Siwan")  # using comma to separate values


