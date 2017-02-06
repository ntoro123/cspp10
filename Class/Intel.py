import random
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

#def mew():
#Example range (10-20, 25, 30-50)
#    rangeList = "10-20, 25, 30-50"
#   maxRange = 100
#    permitRange = 1 << maxRange
#    for range in rangeList.split(","):
#        if range.isdigit():
#            permitRange = setBit(permitRange, int(range))
        else:
           lower, upper = range.split("-",1)
            permitRange = range(permitRange, int(lower), int(upper))
return permitRange

mew()
random_num()