# K pattern 


for row in range(7):
    for col in range(6):
        if col==0 or (row-col==2 and col>1) or row+col==4:
            print("* ", end="") 
        else:
            print(" ",end="")
    print()