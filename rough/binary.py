#### Decimal to binary conversion

##############################
def decimal_to_binary_using_bin(decimal_number):
    # Convert decimal to binary using bin() function and remove the "0b" prefix
    binary_value = bin(decimal_number)[2:]
    return binary_value

# Example usage
decimal_input = 13
binary_output = decimal_to_binary_using_bin(decimal_input)
print(f"Decimal {decimal_input} to Binary is: {binary_output}")

####   Explanation:
### Here bin(decimal_number) converts the decimal number to a binary string, including the 0b prefix.
### [2:] slices off the first two characters ('0b') to return the pure binary representation.


#################################
def decimal_to_binary_string(input_string):
    # Convert each character in the string to its binary representation
    binary_representation = []
    for char in input_string:
        # Convert the character to an integer and then to binary
        binary_value = format(int(char), '04b')  # '04b' formats as 4-bit binary
        binary_representation.append(binary_value)
    
    # Join all binary representations into one string (with a space in between for readability)
    return ' '.join(binary_representation)

# Example usage
input_string = "123"
binary_output = decimal_to_binary_string(input_string)
print(f"Binary representation of '{input_string}': {binary_output}")




#### Binary to Decimal conversion

########################################
def binary_to_decimal(binary_string):
    # Convert binary string to decimal using int() with base 2
    decimal_value = int(binary_string, 2)
    return decimal_value

# Example usage
binary_input = "1101"  # binary for 13
decimal_output = binary_to_decimal(binary_input)
print(f"Binary '{binary_input}' to Decimal is: {decimal_output}")

###  Explanation:
## Here int(binary_string, 2): The int() function takes two arguments: the first is the string to convert, and the second is the base of the number system (in this case, base 2 for binary).
## This will convert the binary string "1101" into the decimal number 13.