Start =  input("Enter a number to start: ")
end = input("Enter a number to start: ")
end = int(end)
start = int(Start)

for blank in range(start - 1, end):
    blank = blank + 1
    if blank % 3 == 0 and blank % 5 == 0:
        print ("fIzzbuzz")
    elif blank % 3 == 0:
        print ("fizz")
    elif blank % 5 == 0:
        print ("buzz")
    else:
        print (blank)