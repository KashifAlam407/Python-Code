# how to write multiplication table 


for i in range(2, 41):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}")
            if j!=10:   ## here if j is equal to 1,2,3,4,5,6,7,8,9 then print \n
                f.write('\n')
    