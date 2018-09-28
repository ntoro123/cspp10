#dictionarys!
from pprint import pprint


d = {
#   key     :   value
}
print(d)

def add(d):
    user_key = input("What is the key you would like to add?: ")
    user_value = input("What is the value for that key?: ")
    d[user_key] = user_value
    pprint (d)
    
add(d)

def remove_key(d):
    user_key = input("What is the key you would like to remove?: ")
    del d[user_key]
    pprint (d)
remove_key(d)

def update(d):
    user_key = input("What is the key you would like to add?: ")
    user_value = input("What is the value for that key?: ")
    user_key_s = input("What would you like to change?: ")
    user_key = user_key_s
    d[user_key] = user_value
    pprint (d)
    
update(d)
quit()