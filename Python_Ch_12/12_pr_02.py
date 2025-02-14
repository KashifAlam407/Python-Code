l = [1,2,3,4,5,6,7,8,9,10]
# for index, item in enumerate(l):
    # if index==2 or index==4 or index==6:   ## This will print the item which is on the index of 3,5,7
    #     print(index,item)
    #     print(f"The {index+1}th element is {item}")

    ###
    # if index%2==0:   ## This will print the odd index item
    #     print(f"The {index+1}th element is {item}")

###
enumerate_l = enumerate(l)
print(list(enumerate_l))


###
# l = ['Python', 'Java', 'JavaScript']
# e = enumerate(l)
# print(list(e))
