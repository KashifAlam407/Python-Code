post = ("harry", "Harry", "HArry", "HARry", "HARRy", "HARRY", "hArry", "hARry", "hARRy", "hARRY", "haRry", "haRRy", "haRRY", "harRy", "harRY", "harrY", "HarrY", "HArrY", "HARrY", "HARRY", "hArrY", "hARrY", "haRrY", "HaRrY", "HARRy" "hArRy")  # i have written this with own method but it can be written with another method
name = input("Enter your name\n")
if name in post:
    print("The given post is talking about harry")
else:
    print("The given post is not talking about harry")