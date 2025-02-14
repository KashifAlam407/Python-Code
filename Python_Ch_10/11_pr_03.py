class Sample:
    a = "Harry"

obj = Sample()  # if we write (obj = Sample) only then it change the class attribute
obj.a = "Vicky"

# Sample.a = "Vikky"   # it change the class attribite

print(Sample.a)  # prints Harry
print(obj.a)   # prints Vikky



