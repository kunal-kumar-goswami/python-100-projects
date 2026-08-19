#Treasure Island 
print('''
*******************************************************************************
             |               |              |               |
 ____________|_______________|______________|_______________|__________
|                          WIZARD'S QUEST - Text Adventure             |
|_____________________________________________________________________|
             |               |              |               |
             |   ,           |      /\      |    ~    ~     |
             |  /_\          |     /__\     |   <o>  <o>    |
             | /___\         |    | __ |    |   /|\  /|\    |
             |               |     ||||     |    |    |     |
*******************************************************************************
''')

print("Welcome, apprentice wizard!")
print("Your mission is to recover the lost Orb of Light from the Enchanted Forest.\n")

# First choice
choice1 = input("You enter the forest and come to a forked path. Do you go 'left' toward the mist or 'right' into the darker woods?\n").lower()

if choice1 == "left":
    # Second choice
    choice2 = input("You walk into the mist and see a river guarded by a sleeping troll.\n"
                    "Do you 'sneak' past him or 'wake' him up to ask for help?\n").lower()

    if choice2 == "sneak":
        # Third choice
        choice3 = input("You quietly cross and find a glowing cave with 3 magical doors: one silver, one green, and one black.\n"
                        "Which door do you open? Type 'silver', 'green', or 'black'\n").lower()
        
        if choice3 == "silver":
            print("The room traps you in an eternal time loop. Game Over.")
        elif choice3 == "green":
            print("You find the Orb of Light shining brightly. You Win!")
        elif choice3 == "black":
            print("You fall into a pit of shadows. Game Over.")
        else:
            print("That door doesn't exist. Game Over.")
    else:
        print("The troll wakes up angry and casts a sleeping curse on you. Game Over.")
else:
    print("You are caught by forest spirits and vanish without a trace. Game Over.")
