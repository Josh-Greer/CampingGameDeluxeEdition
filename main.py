

#Values used for the ending
paranoia = 0
enthusiasm = 0


#question: checks user's response against a list of valid options, used to error check
def question(responses,ans):
    if(responses.count(ans) != 0):
        return True
    else:
        return False

print(f"A Camping Game where you aren't Attacked by Wolves")
name = input("Enter Name: ")

print(f"{name}! Do you like camping? [Yes/No]")
answer = input("")
if (answer.lower() == "yes"):
    print("Great! If you didn't like camping then this game probably wouldn't be too interesting!")
    enthusiasm += 1
elif (answer.lower() == "no"):
    print("oh...")
    print("This game is all ABOUT camping")
    print("Hopefully you enjoy games about camping still")
    print("Well moving on...")
    enthusiasm += 1
else:
    print("Was kind of expecting a yes or a no there...")
    print("That's what the [Yes/No] box was for")
    print("Well moving on...")
print("Time to go off into the woods!")
input("Press enter to enter the woods and begin your amazing camping trip")
print("Wow look you're in the woods now!")
print("[1] 'Wow! I sure do love the woods'")
print("[2] 'I can't 'look' at anything, this is a text based adventure game'")
print("[3] 'There would happen to be any wolves in the woods right?'")
print("(Input '1', '2', or '3' for which dialogue choice you want to make)")
answer = input("")
while(not question(["1","2","3"],answer)):
    answer = input("")

if(answer == "1"):
    print("Yeah! That's the spirit! Love the enthusiasm!")
    enthusiasm += 1

elif(answer == "2"):
    print("Ok fine poor choice of words, but try to be a little imaginative here. You're in the woods.")
    enthusiasm -= 1

elif(answer == "3"):
    print("What? Of course not. Did you read the title? It said there wouldn't be any wolves.")
    paranoia += 1


storyphase1 = [True, False, False, False, False]
checkedforwolvesmessage = "wolves"
while(storyphase1[0]):
    print("What do you want to do now?")
    print("[1] Set up your tent")
    print("[2] Breathe in that forest air")
    print(f"[3] Check around for any {checkedforwolvesmessage}")
    print("[4] Venture the woods")
    answer = input("")
    if (answer == "1"):
        print("Alright cool! Now that everything's prepared you can go out exploring the woods!")
        input("Press enter to continue")
        storyphase1[1] = True
    elif (answer == "2"):
        print("You take a deep breath in")
        print("Smells foresty")
        print("Probably has something to do with you being in a forest")
        input("Press enter to continue")
    elif (answer == "3"):
        if (storyphase1[2]):
            print("You look around for wolves, despite the fact the title told you there weren't any wolves, AND the fact you already checked and there weren't any")
            print("Unsurprisingly, you STILL find no wolves")
            paranoia += 1
            checkedforwolvesmessage = "wolves a third time juuuuuuust to be safe"
            storyphase1[2] = False
            storyphase1[3] = True
        elif (storyphase1[3]):
            print("There. Are. No. Wolves.")
            if checkedforwolvesmessage == "wolves a third time juuuuuuust to be safe":
                paranoia += 2
            checkedforwolvesmessage = "nonexistent wolves"
        else:
            print("You look around for wolves, despite the fact the title told you there weren't any wolves")
            print("Unsurprisingly, you find no wolves")
            paranoia += 1
            checkedforwolvesmessage = "wolves, again"
            storyphase1[2] = True
        input("Press enter to continue")
    elif (answer == "4"):
        if(not storyphase1[1]):
            print("I know you're excited but maybe you should set up your tent first")
            print("Won't be fun if you have to set it up after it gets dark out")
        else:
            print("Alright time to experience the great outdoors!")
            storyphase1[0] = False
            input("Press enter to explore")

print("Now you're deeper in the woods!")


print("What kind of deeper woods activities do you wanna do?")
print("[1] Make a campfire")
print("[2] Swim in the lake")
print("[3] Find a place to hide from wolves")
answer = input("")
while(not question(["1","2","3"],answer)):
    answer = input("")
if(answer == "1"):
    enthusiasm += 1
    print("A classic camping activity! We need to collect wood first. And by 'we' i mean you ")
    input("Press enter to gather wood")
    print("Wow! Good job on getting the wood.")
    print("What will you light it with")
    print("[1] 'A lighter of course'")
    print("[2] 'I was just thinking i'd rub the sticks together until fire, y'know like cavemen!'")
    answer = input("")
    while (not question(["1", "2"], answer)):
        answer = input("")
    if answer == "1":
        print("Good thing you were actually prepared for this!")
        input("Press enter to light the fire")
        print("And there you have a campfire")
        print("It'd probably look cooler if it were night though...")
    else:
        print("uh...")
        print("i don't that's gonna work...")
        print("or we might just be stuck here for while...")
        print("if you don't have anything to actually light it lets just move on...")
    input("Press enter to move on")
elif (answer == "2"):
    print("I'm not sure if thats the best idea...")
    print("Who knows what could be in that lake")
    print("[1] 'I don't care, CANNONBALL'")
    print("[2] Make puppy dog eyes at the narrator")
    print("[3] 'You're right, what if there's sea wolves in the lake?'")
    answer = input("")
    while (not question(["1", "2", "3"], answer)):
        answer = input("")
    if (answer == "1"):
       print("Why don't you-")
       input("Press enter to ignore the narrator and jump in")
       enthusiasm += 1
       print("Well...")
       print("I SUPPOSE it's harmless")
       print("Just don't stay in too long...")
       input("Press enter to exit the lake")
    elif (answer == "2"):
        print("Whats with that face...")
        print("Also if you're trying to face me you know im just a voice right...?")
        print("Well whatever i can't say no to that face...")
        print("Go enjoy the lake")
        input("Press enter to go enjoy the lake")
        print("Alright we should probably head back to the tent now")
        input("Press enter to exit the lake")
    elif (answer == "3"):
        paranoia += 2
        print("Yes exac-")
        print("...")
        print("I'm sorry SEA WOLVES?")
        print("There are no WOLVES PERIOD and there's certainly no SEA WOLVES")
        print("Lets just forget the lake and head back...")
        input("Press enter to forget the lake and head back")
elif (answer == "3"):
    paranoia += 2

    if paranoia <= 4:
        print("There's no wolves here alright?")
        print("Absolutely nothing to be afraid of")
        print("Did you know that nobody's died in these woods in the past year?")
        print("Totally safe")
        print("Now lets move on")
        input("Press enter to move on")
    else:
        print("we're not doing that.")
        print("You're too worried about these wolves that aren't real")
        print("Try to actually enjoy the trip why don't ya?")
        print("C'mon lets find something better to do")
        input("Press enter to find something better to do")

#UnBEARable Route
if (paranoia >= 5 and enthusiasm <= 0):
    print("Honestly i'm starting to think it wasn't even worth coming out here...")
    print("You've just been paranoid about wolves this whole time for no reason")
    print("Maybe you just need rest, you should head back to your tent and rest")
    input("Press enter to head into the tent")
    print(f"OH GOD {name.upper()} THERE'S A BEAR IN THE TENT")
    input("Press enter to JUMP BACK FROM THE TENT BEAR")
    print(f"{name.upper()} IT'S COMING OUT OF THE TENT DO SOMETHING")
    print("[1] Attempt to reason with the bear")
    print("[2] Punch the bear")
    print("[3] Piss yourself in fear")
    answer = input("")
    while (not question(["1", "2", "3"], answer)):
        answer = input("")
    if (answer == "1"):
        print("You tell the bear you have a family and want to live")
        print("Surprisingly, the bear hesitates for a moment, perhaps considering your plea")
        print("Ah wait nevermind it was distracted by a butterfly")
        print("You totally get mauled by the bear after the butterfly leaves")
        print("Game Over.")
    elif (answer == "2"):
        print("You punch the bear in the face as hard as you can")
        print("Now instead of a regular tent bear standing in front of you, you have an angry tent bear")
        print("You totally get mauled by the bear (but the punch was pretty sick though)")
        print("Game Over.")
    elif (answer == "3"):
        print(f"Well {name} have you thought of something to get rid of th-")
        print("...")
        print("I'll take that as a no...")
        print("You totally get mauled by the now mildly disgusted bear")
        print("Game Over.")



#Arson Route
if (paranoia >= 5 and enthusiasm > 0):
    print("You're on your way back to your tent when you see notice something behind you")
    input("Press enter to take a closer look")
    print(f"What're you looking at {name}?")
    print("[1] 'The Wolf.'")
    answer = input("")
    while (not question(["1"], answer)):
        answer = input("")
    print(f"{name} now you're being crazy there's nothing there")
    print("[1] 'Burn The Wolf.'")
    answer = input("")
    while (not question(["1"], answer)):
        answer = input("")
    print("That's a bush that vaguely resembles a wolf PLEASE don't tell me you're going to ignite it")
    input("Press enter to ignite The Wolf.")
    print("You ignite the 'wolf' and it unsurprisingly spread to the whole forest")
    print("Sure you lived but i'm still giving you a game over for burning the forest down")
    print("Game Over.")

#Lost Route
if (paranoia < 5 and enthusiasm < 0):
    print(f"You don't seem to be enjoying the trip {name}")
    print("You should head back and get some rest")
    input("Press enter to head back to the tent")
    print(f"{name} wait im pretty sure it's the other way")
    input("Press enter to head back the other way")
    print("Ok yea i have no idea where it is")
    print("Yea we're totally lost...")
    print("Game Over.")

#Pet Route
if (paranoia < 5 and enthusiasm >= 0):
    print("Honestly i'm starting to think it wasn't even worth coming out here...")
    print("You've just been paranoid about wolves this whole time for no reason")
    print("Maybe you just need rest, you should head back to your tent and rest")
    input("Press enter to head into the tent")
    print(f"OH GOD {name.upper()} THERE'S A BEAR IN THE TENT")
    input("Press enter to JUMP BACK FROM THE TENT BEAR")
    print(f"{name.upper()} IT'S COMING OUT OF THE TENT DO SOMETHING")
    print("[1] Attempt to reason with the bear")
    print("[2] Feed the bear")
    print("[3] Piss yourself in fear")
    answer = input("")
    while (not question(["1", "2", "3"], answer)):
        answer = input("")
    if (answer == "1"):
        print("You tell the bear you have a family and want to live")
        print("Surprisingly, the bear listens and leaves")
        print("Or maybe it got distracted by the butterfly it's chasing")
        print("Either way you live!")
        print("You win camping!")
    elif (answer == "2"):
        print("You feel the bear a little salami that landed in your pocket from lunch")
        print("The bear is pleased with the offering and leaves")
        print("You survived the bear!")
        print("You win camping!")
    elif (answer == "3"):
        print(f"Well {name} have you thought of something to get rid of th-")
        print("...")
        print("I'll take that as a no...")
        print("The bear proceeds to sniff you and leaves right afterwards")
        print("How did that work...")
        print("You win camping... but lose your dignity in the process...")






