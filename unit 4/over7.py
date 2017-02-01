some_list = [2,4,9,6,3,1]

#looping through some list:
for index in range(len(some_list)):
	print("element {} at index {}".format(some_list[index],index))

print("")

#this allows you to change the values
print("original list: {}".format(some_list))
for index in range(len(some_list)):
	some_list[index] = some_list[index] * 10
print("after multiplying by 10: {}".format(some_list))

#here's an easier way, but you can't change the values, nor
#	do you know the indexes
for element in some_list:
	print("the element: {}".format(element))