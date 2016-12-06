seconds = input("Enter a number of seconds: ")
seconds = int(seconds)
x = seconds % 60
y = seconds - x
minutes = y / 60
a = minutes % 60
b = minutes - a
hours = b / 60
seconds_int = int(x)
minutes_int = int(a)
hours_int = int(hours)
print (" {} hours {}  minutes {} seconds.".format(hours,minutes,seconds))