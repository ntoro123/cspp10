import random
health = 100
Backpack = ["Stone", "Plank"]
ally_new = ["Quinn", "Joseph"]
def battle(p_health):
    o_damage = 0
    p_damage = 0
    opponent_hp = 100
    while opponent_hp > 0:
        print ("The opponent hp is")
        print (opponent_hp)
        print ("The player hp is")
        print (p_health)
        rng = 0
        print ("An enemy is in the room ")
        attack = input("Whould you like to attack, defend, run (You can type A or R Just remember there is a chance for failure ")
        print (attack)
        if attack == "A" or attack == "a":
            attack = 1
            print (attack)
        else:
            attack = 0
        rng = (int(random.randint(1,10)))
        p_damage = 0
        if attack == 1 and rng == 1:
            print ("You missed and got hit for 30 damage")
            print (rng)
            p_damage = 30
            p_damage = int(p_damage)
        elif attack == 1 and rng == 2:
            print ("You missed and you got hit for 25 damage")
            print (rng)
            p_damage = 25
            p_damage = int(p_damage)
        elif attack == 1 and rng == 3:
            print ("You missed and you got hit for 20 damage")
            print (rng)
            p_damage = 20
            p_damage = int(p_damage)
        elif attack == 1 and rng == 4:
            print ("You missed and you got hit for 15 damage")
            print (rng)
            p_damage = 15
            p_damage = int(p_damage)
        elif attack == 1 and rng == 5:
            print ("You missed but dogged an incoming attack")
            print (rng)
            o_damage = 0
        elif attack == 1 and rng == 6:
            print ("You landed a hit for 10 damage ")
            print (rng)
            o_damage = 10
        elif attack == 1 and rng == 7:
            print ("You landed a hit for 15 damage ")
            print (rng)
            o_damage = 15
        elif attack == 1 and rng == 8:
            print ("You landed a hit for 20 damage ")
            print (rng)
            o_damage = 20
        elif attack == 1 and rng == 9:
            print ("You landed a hit for 25 damage ")
            print (rng)
            o_damage = 25
        elif attack == 1 and rng == 10:
            print ("You landed a hit for 30 damage ")
            print (rng)
            o_damage = 30
        else:
            rng = 0
        
        opponent_hp = opponent_hp - o_damage
        p_health = p_health - p_damage
        
        if opponent_hp < 1:
            print ("The enemies has been slain")
            return (p_health)
        elif p_health < 1:
            print ("You lost") 
            return 0
            
room = 1
short_key_use = 0
full_key_use = 0
room = 1
enemies = 1
where_you_go = 2990
while where_you_go != 3000:
    where_you_go = input("Where do you want to go type (w,a,s,d or left, right, foward, back) or map, backpack: ")
    if where_you_go == "foward":
        where_you_go = "w"
        full_key_use = full_key_use + 1
    elif where_you_go == "W":
        where_you_go = "w"
        short_key_use = short_key_use + 1
    elif where_you_go == "back":
        where_you_go = "s"
        full_key_use = full_key_use + 1
    elif where_you_go == "S":
        where_you_go = "s"
        short_key_use = short_key_use + 1
    elif where_you_go == "left":
        where_you_go = "a"
        full_key_use = full_key_use + 1
    elif where_you_go == "A":
        where_you_go = "a"
        full_key_use = full_key_use + 1
    elif where_you_go == "right":
        where_you_go = "d"
        full_key_use = full_key_use + 1
    elif where_you_go == "D":
        where_you_go = "d"
        short_key_use = short_key_use + 1
    else:
        short_key_use = short_key_use + 1
    if where_you_go == "w" and room == 1:
        room = 2
        print (room)
        enemies = 1
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        if enemies == 1:
            win_lose = battle(health)
            win_lose = int(win_lose)
            if win_lose > 1:
                print ("You win")
                health = win_lose
            elif win_lose == 0:
                print ("you loss of words")
                break
    if where_you_go == "backpack":
        print (Backpack)
    if where_you_go == "Helper":
        print (ally_new)
    if where_you_go == "map":
        print ("you are in room 1")
    if where_you_go == "s" and room == 2:
        room = 1
        print (room)
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        print ("You have entered a Dark Cave")
    if where_you_go == "room":
        print (room)
    if where_you_go == "health":
        print (health)
    if where_you_go == "info":
        print ("It already says how to move you can type map to pull up a map telling you your location")
    if where_you_go == "w" and room == 1:
        room = 2
        print (room)
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        print ("you have entered a room with A Mirror")
    if where_you_go == "d" and room == 2:                 
        room = 7
        print (room)
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        print ("you have entered a room with A teacher inside it")
        if enemies == 1:
            win_lose = battle(health)
            win_lose = int(win_lose)
            if win_lose > 1:
                print ("You win")
                health = win_lose
            elif win_lose == 0:
                print ("Please tell me why")
                break
    if where_you_go == "d" and room == 1:
        room = 3
        print (room)
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        print ("you have entered emo room")
        Backpack.append("Book")
        print ("You found a book")
    if where_you_go == "a" and room == 1:
        room = 5
        print (room)
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        print ("you have entered cave")
        Backpack.append("Car Keys")
    if where_you_go == "s" and room == 1:
        room = 4
        print (room)
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        print ("you have entered classroom")
    if where_you_go == "a" and room == 7:
        room = 2
        print (room)
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        print ("you have entered hallway")
    if where_you_go == "a" and room == 3:
        room = 1
        print (room)
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        print ("you have entered room 1")
        if enemies == 1:
            win_lose = battle(health)
            win_lose = int(win_lose)
            if win_lose > 1:
                print ("You win")
                health = win_lose
            elif win_lose == 0:
                print ("This is the death of my origin")
                break
    if where_you_go == "w" and room == 4:
        room = 1
        print (room)
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        print ("you have entered white room")
    if where_you_go == "d" and room == 5:
        room = 1
        print (room)
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        print ("you have entered bedroom")
        Backpack.append("Phone")
    if where_you_go == "s" and room == 2:
        room = 1
        print (room)
        print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
        print ("you have entered bottomless pit")