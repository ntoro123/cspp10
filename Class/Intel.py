import random
last_numb = 1000001
x = 0
numb = -1
z = 0
y = 0
def intel():
    m = 1
    while(m <= 100):
        print(m)
        m = m + 1 #increase n by 1
#this generates 5 random numbers     
def random_num():
    XD=[]

XD = random.sample(range(1, 101), 5)


print(XD)
#this will ask the player for an input
def skylit():
    last_numb = 101
while (last_numb > 100):
    last_numb = int(input("Put in a number less than 100 (Max numb you will guess) "))
    if last_numb > 100:
        print ("Your number is too big tell me a smaller one")
XD = random.sample(range(1, 101), 5)
while (numb != XD):
    x = x + 1
    numb = int(input("Tell me the number you guess (1-{}) ".format(last_numb)))
    if numb > XD :
        z = z + 1
        print ("Your number is too high ")
        if z == 4:
            print ("Stop guessing so many high numbers!!! It's annoying!!!")
        if (x > 60):
            break
    elif numb < XD:
        y = y + 1
        print("Your number is too low ")
        if y == 4:
            print("Stop guessing so many low numbers!!! It's annoying!!!")
        if (x > 60):
            print ("You guessed too many times")
            break
        elif numb == XD:
            print ("you guessed the number! It took you {} tries".format(x))
        if (x + 1):
            x = x + 1
            
            print()
        
    else:
        ("You did your life wrong ")
intel()
random_num()
#i have no idea what im doing at thius point