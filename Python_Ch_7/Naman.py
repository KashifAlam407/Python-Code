                                    ## NAMAN  ##
## N
for row in range(7):
    for col in range(5):
        if col==0 or col==5-1 or row==col:
            print("*",end="")
        else:
            print(" ",end="")
    print()

## A
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

## M
for row in range(7):
    for col in range(5):
        if (col==0 or col==6) or (row==col and row<4) or (row+col==6 and row<4):
            print("*",end="")
        else:
            print(" ",end="")
    print()

## A
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

## N
for row in range(7):
    for col in range(5):
        if col==0 or col==5-1 or row==col:
            print("*",end="")
        else:
            print(" ",end="")
    print()