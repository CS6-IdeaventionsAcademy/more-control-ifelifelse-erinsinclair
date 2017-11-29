#Erin J Sinclair
#112917
#Cave Expedition
#Ecscape!

print("Welcome to Cave Expedition! You must find a way out of the cave--but beware. There are many dangers along the way...")
ans = input("You are lost in a cave. There are two passages: left and right. Which way would you like to go?")
if ans=="right":
    ans=input("""You turn right and after a while of walking, you see a beautiful
            river with crystal-clear water. There is a rock bridge streatching
            over it. You also see a boat. Would you like to take the boat or cross
            the bridge?""")
    if ans=="boat":
        print ("""You take the boat upstream for a while. You enter a cavern, with
               many slagmites and salactites. You are distracted by them, so you
               fail to see the waterfall up ahead. But all of a sudden, your boat
               get faster and faster. And before you know it, you are falling down
               an almost vertical waterfall. The boat hits you on the head, so you get
               knocked out and drown.""")
elif ans=="bridge":
    print("hi")
