try: 
    # x = 10/2
    x = 10/0
    print(x)

except Exception as e:
    print(f"An error occurred: {e}") 
    print(e)