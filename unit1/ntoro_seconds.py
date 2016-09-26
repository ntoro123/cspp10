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
seconds_string = str(seconds_int)
minutes_string = str(minutes_int)
hours_string = str(hours_int)
print (hours_string + " hours " + minutes_string + " minutes " + seconds_string + " seconds. ")