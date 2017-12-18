#Erin J Sinclair
#112917
#Cave Adventure
#An exploration adventure game!

def left_cave():
    print("""You walk down the left passage. It is cold and dark.
          The cave opens up to an underground river. There is
          a boat beside it. Do you swim, take the boat, or walk
          along the river?""")
    river_choice=input("Type either walk, swim, or boat:").lower()
    return river_choice
def wrong_answer():
    print("""You just stand there, not making a decision, and eventually
        a dragon comes out for food. It sees you standing there, and roasts
        you with its fire breath. It then takes you home to enjoy. YOU DIE!!!""")
def right_cave():
    print("""You walk down the right passage. It begins to slope downward.
    there is a hole in the floor and a torch in the distance. Do you go down
    the hole or go toward the torch?""")
    torch_choice=input("Please type either torch or hole:").lower()
    return torch_choice
def dragons_lair():
    print("""You unravel your rope and anchor it to the floor. Then you climb down through
    the hole. You can hear a dragon growling nearby. The great beast emerges
    from the shaddows. What do you do?""")
    dragon=input ("Please enter slay or run:")
    return dragon
    
    


print (""" Wlcome to                         
 _________                                                                  
 \_   ___ \ _____   ___  __  ____                                           
 /    \  \/ \__  \  \  \/ /_/ __ \                                          
 \     \____ / __ \_ \   / \  ___/                                          
  \______  /(____  /  \_/   \___  >                                         
         \/      \/             \/                                          
    _____       ___                         __                          
   /  _  \    __| _/___  __  ____    ____  _/  |_  __ __ _______   ____  
  /  /_\  \  / __ | \  \/ /_/ __ \  /    \ \   __\|  |  \\_  __ \_/ __ \ 
 /    |    \/ /_/ |  \   / \  ___/ |   |  \ |  |  |  |  / |  | \/\  ___/  
 \____|__  /\____ |   \_/   \___  >|___|  / |__|  |____/  |__|    \___  >
         \/      \/             \/      \/                            \/  """)
choice=input("""      It's Mideval times. Everything
      is dark. One day you goes out to cut wood,
      and stumble upon a cave enterance.
      You have heard tales of treasure
      guarded by powerfull dragons. You
      know you must not enter, but you
      can not help yourself. You
      peer into the enterance. The cave
      splits into two passages. Do you
      take left one or the right one
      (please enter left or right)?""").lower()
if choice=="left" or choice==" left" or choice == "l" or choice ==" l" or choice == "left passage" or choice==" left passage":
    river_choice=left_cave()
    if river_choice=="boat" or river_choice== " boat":
        print("""You climb into the wooden boat and push off. You do not
              realize there is a leak in the boat, and it sinks. YOU DIE!!!""")
    elif river_choice=="swim" or river_choice== " swim":
        print("""Right when you dive into the water, you realize you
            have never been swimming before.""")
        print("But you find that you are a natural!")
        print("""You swim in the lusciously warm water. You can see
              shining gold ahead. You swim faster and faster until you
              reach a treasure chest! It is full of jewels and gold.
              you take the chest and surface. There is daylight ahead.
              You run towards it. It is an outlet! You run out of the
              cave and all the way back to your house.
              You live in peace and harmony forever more!""")
    elif river_choice=="walk" or river_choice==" walk":
        print("""You start walking along the narrow edge of the river.
              Then you reach a part of the bank that crumbles when you
              put pressure on it. There is now a gaping hole in front of
              you. Gathering your wits, you try to leap across, but hit your
              head on the stone and fall into the water, unconcious. You drown.""")
    else:
       wrong_answer()
elif choice=="right" or choice==" right" or choice=="r" or choice==" r" or choice=="right passage" or choice==" right passage":
    torch_choice=right_cave()
    if torch_choice=="torch" or torch_choice==" torch":
        print("""You walk up to the torch. The flame is bright and warm.
You take it out of its holder. A noise, like a roar, sounds from behind you.
Startled, you drop the torch. It lands on your foot, and the flame consumes you.
You burn to death.""")
    if torch_choice=="hole" or torch_choice==" hole":
        player_choice=dragons_lair()
        if player_choice=="slay" or player_choice== " slay":
            print("""You pull a knife from your pocket and brandish it in the air.
              The dragon roars and a flame shoots from its mouth.
              You run at the dragon, knife raised, and strike right in its
              chest. It shoots a flame at you. It singes your arm, but you stab the dragon
              and it falls to the ground, defeated. You hurry over it. A treasure test
              it sitting at the end of the passage. You open it. It is full of gems and
              gold coins. You turn around and run to the left, where daylight is coming in.
              You run out of the cave and all the way back you your house. You live in]
              preace and harmony forever more!""")
        elif player_choice == "run" or player_choice== " run":
            print("""You turn and flee, but the dragon is on your heels.
        it sends a fireball at you. It misses. The dragon shoots another
        fireball. This one hits you, knocking you to the ground. The flame
        consumes you. You burn to death.""")
else:
   wrong_answer()
    
    
        







