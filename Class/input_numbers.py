#program will take in a bunch of numbers
#until the user types "exit" and then
#prints out all the numbers together

final = " "
inp = input("Enter a number or exit: ")
while(inp != "exit"):
        final = final + inp + " "
inp = input("enter a number or exit: ")
print(final)