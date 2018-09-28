print ("hello")
Binary = input("Enter Number of bits: ")
Binary = int(Binary)
Conversion = (2**Binary) - 1
Conversion_S = str(Conversion)
Binary_S = str(Binary)
print ("Binary {} input {}.".format(Conversion,Binary))
Decemal = input("What number would you like to make?: ")
Dot = int(Decemal)
string = ""
while Dot > 0:
    string = str(Dot % 2) + string
    Dot = Dot // 2
print("The number in binary is: {}".format(string))
New = input("What number would you like to convert?: ")
Bind = New
convert = 0
output = 0
while len(Bind) > 0:
    output = output + Binary * 2 ** convert
    convert += 1
    Bind = Bind[:-1]
print ("The Number is {}".format(output))