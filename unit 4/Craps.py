import random
# function name: roll2dice
#   purpose: genarate a random dice rolls and
#   prints it out, and return the sum
#   arguments: none
#   returns: the sum of the two dice
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum

#funtion name: rules
#   purpose: tells the rules of the game to the player
#   arguments: none
#   returns: none
def rules():
    print

# function name: money_start
#   purpose: Tells the player what they start with
#   arguments: Amount of money you start with
#   returns money
def money_start():
    print ("You have $100")
    return 100
    
# function name: house_start
#   purpose: Tells the player what the house start with
#   arguments: Amount of money house start with
#   returns money
def house_start():
    print ("house have $1000")
    return 1000
    
#function name: Bets
#   purpose: Asked the player to input the amount of bets
#   he would like to lose or win
#   arguments: Bet placed
#   returns: Bets
def bets():
    bets = input("Put in your bets: ")
    return bets

#function name:
def part_one(dice_roll):
    roll = dice_roll()
    if (roll == 2 or roll == 3 or roll == 12):
        return ("lose")
    elif (roll == 7 or roll == 11):
        return ("win")
    else:
        return ("point") 
# print
# return

def game_thing_point(dice_roll, part_one):
    new_roll = 0
    point_roll = dice_roll()
    verify = part_one(dice_roll)
    while (verify == "point") and (point_roll != new_roll or new_roll != 7):
        dice_roll()
        new_roll = dice_roll
        print ("Your roll was {} it rolled {} ".format(point_roll,new_roll))

def craps():
    print("You are going to start with {} dollars".format(money_start()))
    
craps()
    
    
#work in progess

#   If the player rolls a 2, 3, or 12 in this phase, they lose their bet, and the round ends.
# If the player rolls a 7 or 11 in this phase, they win their bet, and the round ends.
# If the player rolls any other number (a 4,5,6,8,9,10), then they continue to Phase 3, with their roll becoming their “point number“
