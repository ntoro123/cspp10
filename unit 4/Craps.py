import random
print("Welcome to the game of Craps!")
print("--------------------------")
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

#funtion name: earning
#   purpose: tells the player if they lost or not
#   arguments: none
#   returns: none

    
# function name: money_start
#   purpose: Tells the player what they start with
#   arguments: Amount of money you start with
#   returns money
def money_start():
    print ("You have $100")
    return 100
    
#function name: Bets
#   purpose: Asked the player to input the amount of bets
#   he would like to lose or win
#   arguments: Bet placed
#   returns: Bets
def bets():
    bets = int(input("how much would you like to bet: "))
    return bets

#function name: Part One
#   
def part_one(roll2dice):
    roll = roll2dice()
    if (roll == 2 or roll == 3 or roll == 12):
        return ("lose")
    elif (roll == 7 or roll == 11):
        return ("win")
    else:
        return ("point") 
# print
# return

def bets_cal():
    bank_b = money_start()
    money = bets()
    while ((money != int(money)) or (money > bank_b) or (money < 1)):
        print("It has to be a whole number, not a negtive, and you need to have enogh money")
        money = bets()

def game_thing_point(roll2dice, part_one):
    new_roll = 0
    point_roll = roll2dice()
    verify = part_one(roll2dice)
    while (verify == "point") and (point_roll != new_roll or new_roll != 7):
        roll2dice()
        new_roll = roll2dice
        print ("Your roll was {} it rolled {} ".format(point_roll,new_roll))

def craps():
    print("You are going to start with {} dollars".format(money_start()))
    int(input("how much would you like to bet: "))
    bank_b = money_start()
    money = bets()
    while ((money != int(money)) or (money > bank_b) or (money < 1)):
        print("It has to be a whole number, not a negtive, and you need to have enogh money")
        money = bets()
    roll = roll2dice()
    if (roll == 2 or roll == 3 or roll == 12):
        print("You lost")
        check = 0 #lose
    elif (roll == 7 or roll == 11):
        print("You Win")
        check = 1 #win
    else:
        check = 2 #point
        print("You didn't land the things ... POINT ROUND")
            
    new_roll = 0
    point_roll = roll
    while (check == 2) and (point_roll != new_roll and new_roll != 7):
        new_roll = roll2dice()
        print ("Your roll was {} it rolled {} ".format(point_roll,new_roll))
        if point_roll == new_roll:
            print("You win your first and Second number matchs")
        elif new_roll == 7:
            print ("You lost you rolled 7")
        else:
            print("It's a draw let's keep going until you ether win or lose")
            input("Press Enter to continue...")
    
        
craps()
    
    
#work in progess

#   If the player rolls a 2, 3, or 12 in this phase, they lose their bet, and the round ends.
# If the player rolls a 7 or 11 in this phase, they win their bet, and the round ends.
# If the player rolls any other number (a 4,5,6,8,9,10), then they continue to Phase 3, with their roll becoming their 