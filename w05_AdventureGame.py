"""
File: w05_Prove_AdventureGame.py
Author: Leah Tajon

Overview: 
In a text-based adventure game, the user is presented a scenario with different options. 
Depending on the option they choose, they have different consequences, which in turn present
different choices for the next action. 
"""

print("WELCOME TO THE ADVENTURE GAME! Let's begin.\n")
print("""You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. 
Which one do you want to pick up?
""")
level_1 = input("MATCH OR FLASHLIGHT? >>> ")

if level_1.lower() == 'match':
    print("\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated.")
    print("You see a large grizzly bear, and then the match burns out."
    "\nDo you want to RUN, HIDE behind a tree, or FIGHT the bear?")

    level_2 = input("\nRUN, HIDE or FIGHT? >>> ")
    if level_2.lower() == 'run':
        print("\nYou run as fast as you can."
        "You look back and the bear is chasing you behind.\n"
        "While frantically running, you see a dark and circular cave in a distant.\n"
        "Do you want to go in the cave?")

        level_3 = input("\nYES or NO? >>> ")
        if level_3.lower() == 'yes':
            print("\nThe cave shut as you go inside. Then, you see a glowing stick under a rock.\n"
            "You push the rock and pick up the stick. You wave the magical stick and POOF...you\n"
            "became a wizard!\n\n"
            "THE END")
        elif level_3.lower() == 'no':
            print("\nYou're scared of the dark cave so you keep on running.\n"
            "But the bear catch up on you. It grabs you by the arm and tries to attack but\n"
            "a beautiful fairy appears and she casts a spell on the bear.\n"
            "The bear is gone and you are safe at last!\n\n"
            "THE END.\n")
    elif level_2.lower() == 'hide':
        print("\nWhile in hiding, you notice that the tree is not an ordinary tree\n"
        "for it bears two types of fruits, a red fruit and a yellow fruit.\n"
        "You like to try them both but which one do you want to eat first?\n"
        "The RED fruit or the YELLOW fruit?")

        level_3 = input("\nRED or YELLOW? >>> ")
        if level_3.lower() == 'red':
            print("\nYou pick up the red fruit and eat it. Suddenly, you feel drowsy and weak.\n"
            "You lean your back against the tree and fall into a deep sleep.\n"
            "You didn't know that the red fruit was a cursed fruit.\n"
            "Now, only a true love's kiss can wake you up.\n\n"
            "THE END.")
        elif level_3.lower() == 'yellow':
            print("\nYou pick up the yellow fruit and eat it. You become mighty and invincible!\n"
            "You walk up to the bear, beat it up, and toss it to the northern sky.\n"
            "The bear is now a constellation!\n\n"
            "The End.\n")
    elif level_2.lower() == 'fight':
        print("\nYou pick up a fight, but the bear is a black belt Karate master so he knocked you out."
        "\nYou are no match for the mighty bear.GAME OVER!\n")
        

elif level_1.lower() == 'flashlight':
    print("\nYou pickup the flashlight and turn in on.\nYou see the pathway lit up in front of you,"
    "\nbut you thought you also heard something off to the side.\nDo you want to FOLLOW the path or LOOK in the trees for"
    "the thing that made the noise?")
    
    level_2 = input("\nFOLLOW or LOOK? >>> ")
    if level_2.lower() == 'follow':
        print("\nWhile walking down the path, you notice a key on the ground.\n"
        "You pick it up, wipe the dust off and put it in your pocket.\n"
        "When you reach the end of the path, you notice the two doors in front of you.\n"
        "The first door is on the RIGHT and the other one is on the LEFT.\n"
        "Both of them are locked so you get the key in your pocket.\n"
        "Which door should you open? The RIGHT door or the LEFT door?\n"
        )

        level_3 = input("LEFT or RIGHT? >>> ")
        if level_3.lower() == 'right':
            print("\nYou unlock the door and you enter into the room.\n"
            "The room is filled with treasures and gold.\n"
            "The room keeper tells you that everything in the room is yours.\n"
            "Yay! You're finally rich.\n\nTHE END.\n")
        elif level_3.lower() == 'left':
            print("\nYou unlock the door and you enter into the room.\n"
            "The room is filled with money and precious stones.\n"
            "The room keeper tells you that everything in the room is yours.\n"
            "Yay! You're finally rich.\n\nTHE END.\n")

    elif level_2.lower() == 'look':
        print("\nYou look in the trees and see a wild boar feeding on leaves.\n"
        "Will you KILL the boar or FEED it with other leaves and grass?\n")

        level_3 = input("KILL or FEED >>> ")
        if level_3.lower() == 'kill':
            print("\nYou're hungry so you kill the boar and roast it.\n"
            "You want to finish it at once so you devour its meat, but the food gets stuck in your throat.\n"
            "You call for help but no one came. You pass out and die!\n\nGAME OVER!\n")
        elif level_3.lower() == 'feed':
            print("\nYou feed the boar with leaves, grasses and fruits.\n"
            "The pig is gentle and nice to you. You adopted the pig and called it 'BABE'.\n\nTHE END.\n")
