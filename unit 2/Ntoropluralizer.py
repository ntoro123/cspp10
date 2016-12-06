noun = input("Enter a noun: ")
number = int(input("Enter a number: "))

if noun[-2:] == "fe" and (number > 1 or number == 0) :
    print("{} {}".format(number,noun[:-2]+"ves"))
elif noun[-2:] == "fe" and (number == 1):
    print("{} {}".format(number,noun))
elif noun[-1:] == "y" and (number > 1 or number == 0) :
    print("{} {}".format(number,noun[:-1]+"ies"))
elif noun[-1:] == "y" and (number == 1):
    print("{} {}".format(number,noun))
elif noun[-2:] == "sh" or noun[-2:] == "ch" and (number > 1 or number == 0) :
    print("{} {}".format(number,noun+"es"))
elif noun[-2:] == "us" and (number > 1 or number == 0):
    print("{} {}".format(number,noun[:-2]+"i"))
elif noun[-2:] == "ay" or noun[-2:] == "ey" or noun[-2:] == "oy"  or noun[-2:] == "uy" and (number > 1 or number == 0) :
    print("{} {}".format(number,noun[:-1]+"s"))
else:
     print("{} {}".format(number,noun +"s"))
     
#I have made this program and change any word to the correct plural.
#I decided to go with if statements because it seemed to organize it.
#I thought I did an amazing job at organization. I wish I could have 
#made the code shorter
#Is it possable you can make this code a lot shorter?