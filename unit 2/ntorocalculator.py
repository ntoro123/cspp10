c = input("enter a three digit equation: ")

digit_one = int(c[0])
operator = c[1]
digit_two = int(c[2])


if operator == "+":
    result = digit_two + digit_one
    print("The result is {}.".format(digit_one+digit_two))
elif operator == "-":
    result = digit_two - digit_one
    print ("The result is {}.".format(digit_one-digit_two))
elif operator == "*":
     result = digit_two * digit_one
     print ("The result is {}.".format(digit_one*digit_two))
elif operator == "/":
     result = digit_two / digit_one
     print ("The result is {}.".format(digit_two/digit_one))
elif operator == "%":
     result = digit_two % digit_one
     print ("The result is {}.".format(digit_one%digit_two))

#This code was more about creating a calculater. A simple one at that
#I felt this one was the better of the two because it just looks neat
#No problems there really just it does what it does.
#Why doesnt the X go away?