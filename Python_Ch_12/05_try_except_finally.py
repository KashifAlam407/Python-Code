try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    #exit()
finally:  
    print("we are done")  ## executed if we exit the programm or if we not exit the program

print("Thanks for using the program") ## if we exit the programm then it does not execute