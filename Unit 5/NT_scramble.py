#For this code we are working on currently we need to have that takes in a phrase or sentence and scrambles every word,
#keeping only the first letter and the last letter the same. For this code I will break it down into two functions and
#have every word scrambled in some type of way. In a way I would start by making a shuffle function then continue by breaking it down into working
#I will import random in the beginning and then use it to genarate a random number I then 
import random
word_1 = 0
word = "Phrase"
def scramble_word():
    list_1=[]
    
    if len(word) == 1:
        return (word)
    if len(word) == 2:
        return (word)
    if len(word) == 3:
        return (word)
    else:
        word_1 = 1
        
    if word_1 == 1:
        half_word = word[1:-1]
        print (half_word)