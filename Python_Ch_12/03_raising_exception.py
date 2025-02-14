def increment(num):
    try:
        return int(num) + 1

    except:
        raise ValueError("This is not good - Kashif")

a = increment(89)
# a = increment("adofd")    # Raise an error 
print(a)