for row in range(8):
    for col in range(7):
        if (col==0 or col==6) or (row==col and row<4) or (row+col==6 and row<4):
            print("*",end="")
        else:
            print(" ",end="")
    print()
