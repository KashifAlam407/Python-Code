codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')

# exec(codeObejct)   ## execute
eval(codeObejct)  ## evaluate

# print(codeObejct)   ## not work
