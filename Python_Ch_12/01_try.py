### 1
while(True):   
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:   ## it gets executing or trying automatically without program crash
        print("Trying...")
        a = int(a)
        if a>6:
            print("You entered a number greater than 6")

    except Exception as e:
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing this game")


### 2
# print("Press q to quit")
# a = input("Enter a number: ")
# if a == 'q':
#     break

# try:
#     print("Trying...")
#     a = int(a)
#     if a>6:
#         print("You entered a number greater than 6")
# except Exception as e:
#     print(f"Your input resulted in an error: {e}")

# print("Thanks for playing this game")


try: 
    # x = 10/2
    x = 10/0
    print(x)

except Exception as e:
    print(f"An error occurred: {e}") 
    print(e)
    print("Type of error:", type(e))
    print("Type of error:", type(e).__name__)
    # print("Zero Division Error")

else:
    print("No error occurred, this is the else block")

finally:
    print("This is the finally block, it always executes")



### 