#Import libraries and modules
import random

#Define randomizer function
def chance(probability):
    rand = random.randint(0, 10)
    if (rand <= probability * 10):
        return True
    else:
        return False

#Define game-over function
def endGame(deathLog, ending):
    print(deathLog + "\n\n" + "Ending: " + ending.upper() + "\n\n")
    exit

#Pagebreak
print("\n\n\n\n\n\n\n\n\n\n\n\n")

#Get player info
choice = input("Do you want to customize your adventure?\n(1) for yes, (0) for no.\n\n")
if (choice == "1"):
    name = input("Great! What do you wish to be called?\n\n").capitalize()
    choice = input("And what pronouns do you prefer?\n(1) for he/him/his, (2) for she/her/her, (3) for they/them/their\n\n")
    if (choice == str(1)):
        pronoun = ["he", "him", "his"]
    elif (choice == str(2)):
        pronoun = ["she", "her", "her"]
    else:
        pronoun = ["they", "them", "their"]
else:
    name = "Kevin"
    pronoun = ["he", "him", "his"]

#Replay cycle
replay = True
while (replay == True):

    #Pagebreak
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    
    #Initialize value
    curiosity = random.randint(3,5)
    knowledge = 0
    mental = random.randint(4,6)
    oxygen = random.randint(3,5)
    hygiene = 5
    hunger = random.randint(3,5)
    thirst = random.randint(3,5)
    time = 0

    #Initialize variables
    action = []
    checkpoint = 0
    optionalStoryline = []
    gameOver = False

    #Story
    print(f"{name} swallowed.\n\nIt's been 5 days since {pronoun[0]} had any food. {pronoun[0].capitalize()} was dirty, starving, cold, and miserable in the tiny hole {pronoun[0]}'d dug out for {pronoun[1]}self. {pronoun[0].capitalize()} wanted out of there, but {pronoun[0]} didn't dare to, not with the creepy creature wandering about.\n\n")

    #Choice 0
    choice = input(f"Should {pronoun[0]} take a peek outside (1), or remain in hiding (0)?\n\n")
    action.append(int(choice))
    print("\n\n\n")

    #Action 0.0 immediate consequences
    if (action[0] == 0):
        if (chance(0.85)):
            curiosity += 1
        if (chance(0.75)):
            oxygen -= 1
        optionalStoryline.append("")
        optionalStoryline.append("")

    #Action 0.1 immediate consequences
    if (action[0] == 1):
        curiosity -= 1
        knowledge += 1
        if (chance(0.3)):
            mental -= 1
        oxygen += 1
        hygiene -= 1
        optionalStoryline.append(", slimy,")
        optionalStoryline.append(f" It screeched once the other day, when {name} mustered the courage to pry open a hole the size of {pronoun[2]} finger to get a peek outside.\n\nThe sound was otherworldly, merely in the sense that it was unnatural. It chilled {pronoun[1]} down to the bones and set all of {pronoun[2]} nerves on fire. It scratched {pronoun[2]} eardrums out, and it rattled {pronoun[1]} deeply.\n\nThere was some sort of slimy substance leaking through the hole {pronoun[0]} made after {pronoun[0]} plugged it back up. That was how {pronoun[0]} knew the creature was slimy.")

    #Story
    print(f"{pronoun[0].capitalize()} never really got a good look at it. All {pronoun[0]} knew was that it was big{optionalStoryline[0]} and heavy enough to leave horrible dragging sound on the ground wherever it went.{optionalStoryline[1]}\n\n{name} has no recollection of how {pronoun[0]} got here, but {pronoun[0]} knew {pronoun[0]} needed to find a way out.\n\nThe beast lingers, though…\n\n")

    #Choice 1
    choice = input(f"Should {pronoun[0]} make a run for it (0), or keep on waiting just a bit longer (1)?\n\n")
    action.append(int(choice))
    print("\n\n\n")

    #Action 1.1 immediate consequences
    if (action[1] == 1):

        #Story
        print(f"Day turned into night and back into day, but {name} dared not make {pronoun[2]} way out of the hole. If the creature was still lingering out there, and {pronoun[0]} knew it was, then {pronoun[0]} was as good as dead the moment {pronoun[0]} left the safety of {pronoun[2]} hiding hole. The best, and most logical, course of action for {pronoun[1]} to take is to wait it out. Surely, the beast would eventually lose interest in {pronoun[1]} and walk away, right?\n\n")

        #Wait loop
        init = 0
        while (action[1] == 1 and not gameOver):
            curiosity += 1
            mental -= 1
            if (chance(0.7 + init)):
                oxygen -= 1
            if (chance(0.6 + init)):
                thirst -= 1
            if (chance(0.5 + init)):
                hunger -= 1

            #Check for asphyxiation
            #Consequence 1.1a:  If (oxygen <= 0) => !Game over: death by asphyxiation!
            if (oxygen <= 0 and not gameOver):
                gameOver = True
                deathLog = f"{pronoun[0].capitalize()} couldn't breathe.\n\n{name} tried to stop {pronoun[1]}self from panicking, but only succeeded in breathing even quicker. {pronoun[0].capitalize()} could almost feel the rest of the precious oxygen reserve in the tiny burrow being used up by {pronoun[2]} lungs, squeezing helplessly to extract whatever sustenance it could from the stale, damp air, but even that wasn't enough. Spots of colour started swimming in {pronoun[2]} field of vision, {pronoun[2]} ears buzzed with static, and {pronoun[2]} heart rate grew sluggish once the initial realization had settled down.\n\n{name} was so tired. {pronoun[0].capitalize()} would just take a real quick nap right here, on this particularly comfortable spot of dirt that felt so soft it might have been a feather-lined bed, and get in some eye shut. {pronoun[0].capitalize()} could even feel the weight of a warm blanket settling on top of {pronoun[2]} limbs, such a soft and fuzzy blanket that {pronoun[0]} couldn't help nuzzle in and relish in the sentiments for a tiny bit longer…"
                ending = "vacuum tight"
                endGame(deathLog, ending)
                break

            #Check for dehydration
            #Consequence 1.1b:  If (thirst <= 0) => !Game over: death by dehydration!
            if (thirst <= 0 and not gameOver):
                gameOver = True
                deathLog = f"{pronoun[2].capitalize()} entire body burned with an insufferable heat. {pronoun[2].capitalize()} throat was so dry it felt like sandpaper, and {pronoun[2]} lips were cracked to the point {pronoun[0]} could taste {pronoun[2]} own blood anytime {pronoun[0]} inhaled.\n\nAt this point, {pronoun[0]} would kill just for a single drop of water. {pronoun[0].capitalize()} was so hot {pronoun[2]} body would probably be drenched in sweat, had it any excess water to shed. {pronoun[2].capitalize()} saliva had all dried up hours ago, and {pronoun[2]} tongue had barely any strength left to move. {pronoun[0].capitalize()} tried to lick the dirt for any last droplet of mist {pronoun[0]} could consume, but even the sand felt dry and harsh on {pronoun[2]} taste buds.\n\nEach breath {pronoun[0]} exhaled was an expensive waste of invaluable water, so {pronoun[0]} tried {pronoun[2]} best to slow down {pronoun[2]} heart rate and kept {pronoun[2]} mind sedentary. {pronoun[0].capitalize()} thought about a source of flowing water, a stream of fresh, clear and sweet liquid, how refreshing it would feel rushing down {pronoun[2]} throat with each gulp, the way it would cool {pronoun[1]} down and quench the insatiable thirst clawing up {pronoun[2]} guts, the way it would heal {pronoun[2]} chapped lips and wash away the parched flakes of {pronoun[2]} own dried skin…"
                ending = "dry twig"
                endGame(deathLog, ending)
                break

            #Check for starvation
            #Consequence 1.1c:  If (hunger <= 0) => !Game over: death by starvation!
            if (hunger <= 0  and not gameOver):
                gameOver = True
                deathLog = f"{pronoun[2].capitalize()} stomach hurt.\n\nIt hurt so bad, all {pronoun[0]} wanted to do was to curl up and die. It felt as though each and every inch of {pronoun[2]} guts were intertwined into a tight knot, only to be squeezed and stretched at the same time. {pronoun[2].capitalize()} stomach must be digesting itself, with the mere amount of acid it must have secreted while {pronoun[0]} was deprived of a single bite of nutrition for days ongoing. {pronoun[0].capitalize()} barely had the energy to do anything other than stare hopelessly into the patch of dirt in front of {pronoun[1]} and imagine it as being something less depressing.\n\nA tasty steak hamburger, perhaps?\n\nIt smelled so good, with the fresh, soft bun and medium rare patty, still sizzling with fresh oil and dripping red hot sauce all over. It felt so real, so close, so within reach, that {name} could almost just reach out and snatch it…"
                ending = "extreme diet"
                endGame(deathLog, ending)
                break

            #Check for sanity
            if (mental <= 0 or curiosity >= 8):
                action[1] = 0
                mental -= 2
                print(f"{name} tried to force himself to wait a bit longer, but {pronoun[2]} curiosity got the better of {pronoun[1]}. Impulsively, {pronoun[0]} made the decision to throw all caution to the wind and make a run for it.")
                break
            
            #Check if beast had left
            if (chance(0.1 + init*0.5)):
            
                #Case 1.1e.0: Beast had left
                checkpoint += 1
                break

            print(f"{name} settled down and waited for another day.\n\nThe beast still lingered, though...\n\n")

            init += 0.1

            #Choice
            choice = input(f"Should {pronoun[0]} keep on waiting (1), or just make a run for it (0)?\n\n")
            print("\n\n\n")
            if (choice == str(0)):
                action[1] = 0
                break


    #Action 1.0 immediate consequences
    if (action[1] == 0 and checkpoint == 0 and not gameOver):
        stamina = hunger * 0.5 + thirst * 0.7 + mental * 0.2
        stamina -= 2
        checkpoint += 1

    #Checkpoint 1
    if (checkpoint >= 1 and not gameOver and action[1] == 0):
        #Story
        print(f"Taking a deep breath, {name} bursted from the hole {pronoun[0]} was hiding and made a run for it, eyes squeezing shut as they burned with heightened sensitivity from adjusting to almost absolute darkness for so long. It appeared to be daytime outside, just as luck would have it.\n\nHe ran and ran and ran, hearing the familiar screeching sound of the beast giving chase right on {pronoun[2]} tail, but {pronoun[0]} ignored it and kept pushing forward. {pronoun[0].capitalize()} was quickly drained of all of {pronoun[2]} strength from an empty stomach and a parched throat...\n\n")
        
        #Consequence 1.0a: mental * 10% chance of retaining sanity 
        if (chance(mental * 0.3)):

            #Case 1.0a.1: Sanity retained => Continue
            #Story
            print(f"...but at the very least {pronoun[0]} still retained whatever left of {pronoun[2]} sanity, enough to understand that being caught effectively spells out the end for {pronoun[1]}.")
            
            #Consequence 1.0b: stamina * 20% chance of outrunning beast
            if (chance(stamina * 0.2)):
                
                #Case 1.0b.1: Outran beast => Continue
                #Story
                print(f"And {pronoun[0]} can't give up just that easily, no matter how tired {pronoun[0]} is.\n\nSurvival instincts kicking in, {pronoun[0]} experienced a final boost of stamina that powered {pronoun[1]} through the nearest cave opening into a mountain cliff, {pronoun[2]} slender frame just barely squeezing through the tight crack between the ledge and the wall.\n\nThe creature slammed against the wall, the sound of the impact muffled, but subdued. It couldn't fit in through the tiny crack.")
                exit
            
            #Case 1.0b.0: Beast caught up => !Game over: death by being caught and eaten by beast!
            else:
                gameOver = True
                deathLog = f"{name} could hear the sound of the creature approaching {pronoun[1]}, and tried as {pronoun[0]} might, {pronoun[0]} just couldn't seem to shake it off. It was much quicker than {pronoun[1]}, its body slithering on the ground with deadly precision as opposed to {pronoun[2]} clumsy steps, and it wasted no time taking advantage of their speed difference.\n\nAt that point, it had become palpably clear to both prey and predator who the victor of their impromptu game of tag was, ultimately. Whatever {name} tried to do, {pronoun[0]} would only be further prolonging {pronoun[2]} inevitable suffering. The beast seemed pleased that its prey was putting up a fight, turning even more tenacious with each sharp twist, turn and dove {name} executed in a desperate effort to turn the tides. It let out a screech, and this time the sound was right on {name}'s heels.\n\nFrom then on, it was solely a matter of time. {name} chanced a look over {pronoun[2]} shoulder, only to be met with a pair of wide open jaws, filled to the edge with glimmering sharp-edged canines and dentas.\n\nAs it closed the distance with a mighty lunge, {name} closed {pronoun[2]} eyes and braced himself.\n\nThe blood splatter felt warm to {pronoun[2]} skin as the creature made quick work of {pronoun[2]} frail, malnourished body.\n\n"
                ending = "crunchy snack"
                endGame(deathLog, ending)
            exit

        #Case 1.0a.0: Sanity lost => !Game over: death by giving up and being eaten by beast!
        else:
            gameOver = True
            deathLog = f"{name} dropped to the ground and remained there. \"What's the point?\", {pronoun[0]} thought to himself. Even if {pronoun[0]} somehow managed to escape the beast, {pronoun[0]} still had no clue where {pronoun[0]} was. {pronoun[0].capitalize()} had no food, no supply, no sense of direction, no tools, no weapons, and no hope of making it out of there alive. Dying was as good as an inevitability by that point, so what does {pronoun[0]} care about being chomped on by a flesh-hungry beast? If anything, {pronoun[0]} was doing it a solid favour by offering it a nice meal, sacrificing whatever left of {pronoun[2]} walking corpse to a creature that stood a much better chance than {pronoun[1]} at survival.\n\nTurning around to face the beast, {pronoun[0]} welcomed its sharp talons and pointy dentas with open arms, embracing the pain of being munched in half as it was the last thing {pronoun[0]} could feel."
            ending = "juicy snack"
            endGame(deathLog, ending)

    #Continue       
    if (not gameOver and checkpoint >= 1):
        
        #Course 1.1e.0
        if (action[1] == 1):
            
            #Story
            print(f"{name} reared from the hole, to {pronoun[2]} utmost relief, to find no beast in sight. Sweeping {pronoun[2]} eyes over {pronoun[2]} surroundings, {pronoun[0]} spotted an opening in a cliffside nearby. The sun had almost completely disappeared below the horizon, so {name} decided to chance it and dash head-first for the cave.")

            #Consequence 1.1e.0
            if (chance(0.8)):

                #Case 1.1e.0.0: Beast ambushed => !Game over: death by being ambushed by beast!
                gameOver = True
                deathLog = f"The cave opening is so close within reach now. Pushing himself to the absolute furthest {pronoun[0]} was humanly capable of, {name} rushed the few last steps--\n--only to be swooped into the air and tossed back like a rag doll.\n\nRolling on the ground, {pronoun[0]} lost the battle to the unstoppable force of inertia, earning himself deep scratches from the rough terrain that marred up every inch of {pronoun[2]} exposed skin. Though at that point, the pain barely even registered in {pronoun[2]} mind anymore.\n\n{name} dreaded to look up, already knowing what {pronoun[0]} would find, but did so anyway.\n\nThere stood the beast in all its former glory, jaws agape and growling menacingly, predatory eyes trailed on {pronoun[2]} frail body as if observing a delicious, mouth-watering snack.\n\nAnd without any further warning, it swooped forward, engulfing {pronoun[1]} whole in one monstrous chomp.\n\n"
                ending = "it’s not that simple"
                endGame(deathLog, ending)

            #Case 1.1e.0.1: Beast truly gone => Continue
            else:

                #Story
                print(f"Finally, {pronoun[0]} made it, stepping into the darker unlit interior of the rocky formation and leaving the dangerous creature far behind.")
        
        #Continue
        if (not gameOver):
            
            #Consequence 0.1
            if (action[0] == 1):

                #Story
                print(f"Already knowing the creature's slimy nature, {name} knew better than to dawdle. {pronoun[0].capitalize()} gathered the surrounding foliage and grabbed whatever dry twigs {pronoun[0]} could, then used them to patch up the tight opening as best as {pronoun[0]} could, in case the beast still tried to follow {pronoun[1]}.\n\n")
                time = 10

            #Consequence 0.0
            else:

                #Story
                print(f"{pronoun[0].capitalize()} was safe, at least for now.\n\n")
                mental += 1

    #Outtro
    if (not gameOver):
        print("To be continued...\n\n")

    #Replay prompt
    choice = input("\n\nDo you want to replay?\n(1) for yes, (0) for no.\n\n")
    if (choice == "1"):
        replay = True
    else:
        replay = False