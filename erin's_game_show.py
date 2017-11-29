#Erin J Sinclair
#112817
#Praying Mantis Game Show
#Open a door and see what you find...
play=True
print ("Welcome to the Praying Mantis Game Show! Pick a door, any door, and see what you find!")
while play==True:
    player_door = input ("Which door would you like to open? The Raven's door, the Oaken door, the Red door, or the Spruce door?")

    if player_door== "the Raven's door":
        print ("You won a vacation to a rainforest! You will get to stay at a five-star hotel!")
    elif player_door=="the Oaken door":  
        print ("You won a lifetime supply of chocolate! You will receive one shipment of twenty chocolates every week for five years!")
    elif player_door=="the Red door":
        print("You won one million pounds of any flavor of ice cream!")
    elif player_door=="the Spruce door":
        print("You won a set of 50 books! Genre of choice.")

    ans = input("Would you like to play again(True or False)?")
    if ans!="True":
        play = False
        print("""Thank you for participating in the Praying Mantis Game Show!
                You will receive lovely parting gifts, including a goat, a pig, a cow,
                and a sheep!""")
       

              
