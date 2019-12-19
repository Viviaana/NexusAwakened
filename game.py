answer_a = ["a", "A"]
answer_b = ["b", "B"]
answer_c = ["c", "C"]
answer_d = ["d", "D"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
inventory = ["no items"]
door_code = ["1976", "1 9 7 6"]


import time
import sys
import random
import os


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def title():
    print("*         __                      *                   ")
    print("      /\ \ \_____  ___  * _ ___                     * ")
    print("     /  \/ / _ \ \/ / | | / __|               *      ")
    print("    / /\  /  __/>  <| |_| \__ \                     ")
    print("    \_\ \/ \___/_/\_\\__,_|___/        *            * ")
    print("                     *                           ")
    print("         _    *           _                       _") 
    print("        /_\__      ____ _| | _____ _*__   ___  __| |")
    print("       //_\\ \ /\  / / _` | |/ / _ \ '_ \ / _ \/ _` |  *")
    print("      /  _  \ V  V / (_| |   <  __/ | | |  __/ (_| |")
    print("    * \_/ \_/\_/\_/ \__,_|_|\_\___|_| |_|\___|\__,_|")
    print("                    *              *")
    print("                               *             *")
    print("            *")
    time.sleep(1)
    start_game()

def start_game():
    print(" ")
    print("Are you ready to begin? [Y/N]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        title()
    else:
        start_game()

def intro():
    time.sleep(1)
    print(" ")
    delay_print("And when the fate of their planet became irreversible, they built ships.\n")
    print(" ")
    time.sleep(1)
    delay_print("The last of the great Seed Ship drifted silently across the gulf of space,\n")
    delay_print("thousands still frozen within her beating core, the Chosen.\n")
    print(" ")
    time.sleep(2)
    delay_print("You are Nexus AI, built  to serve, built to save, built to protect the Chosen\n")
    delay_print("Cortex Online, Visual input detected, shard power nominal.\n")
    print(" ")
    time.sleep(2)
    delay_print("Across the room lies an injured Chosen.\n")
    delay_print("Bloodied ID Card around her neck, She's awake but she doesn't respond to your movements.\n")
    print(" ")
    wake_up()

def wake_up():
    print("Do you activate the medical protocol? [Y/N]")
    choice = input(">>> ")
    if choice in yes:
        time.sleep(1)
        print("")
        print("As you approach the Chosen she raises a glowing power shard and with a scream melts your brain cortex.\n")
        death_screen()
    elif choice in no:
        option_no_medprod()
    else:
        print("You must choose an option")
        wake_up()
        
    
def option_no_medprod():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print ('                                                                 ')
    print ('                        .~_~.                                    ')
    print ('                      ,^ .~ ~. ^.                                ')
    print ('                     / .^ |   ^. \                               ')
    print ('                   Y  /   |     \  Y            ___.oOo.___      ')
    print ('                   | Y    |      Y |           |           |     ')
    print ('                   | |    |      | |           |       , @ |     ')
    print ('                   | |   _|___   | |           |     /\    |     ')
    print ('                   | |  /____/|  | |           |_____||____|     ')
    print ('                   |.| |   __/|__|.|           |           |     ')
    print ('                   |.| |   __/|  |.|          _|___________|_    ')
    print ('                   |:| |   __//  |:|          ^^^^^^^^^^^^^^^`   ')
    print ('                   |:| |_____/   |:|                             ')
    print ('    _______________|_|/          |_|____________________________ ')
    print ('    _______________]H[           ]H[_____________________________')
    print ('                    /             \                              ')
    print ('                                          ( ;^{)=                ')
    print ('               ~~~~~                                <)))))>      ')
    time.sleep(1)
    print(" ")
    print("In shock you exit the power room and move down the corridor,")
    print("parts of destroyed Nexus units litter the floor, dirt and grime hang to the walls.")
    print(" ")
    time.sleep(1)
    print("You reach the connection door at the bottom, unusually it's Chosen ID locked.")
    time.sleep(1)
    print("Confused you search the corridor, you locate:\n")
    time.sleep(1)
    print("A. discarded power shard")
    print("B. a damaged Holo-Drive")
    print("C. a pile of conducting wire")
    item_choice()

def item_choice():
    print("\n What do you collect? [A/B/C]")
    choice = input(">>> ")
    if choice in answer_a:
        print(" ")
        print(" ")
        print(" ")
        print("The Unstable Shard erupts and the explosion tears your entire body apart")
        death_screen()
    elif choice in answer_b:
        option_holodrive()
    elif choice in answer_c:
        option_conductingwire()
    else:
        print("You must choose an option")
        item_choice()

def option_holodrive():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("'If I can power the cortex, maybe I could gain some answers,'")
    print("You say to yourself as you attach it to your rear pack.")
    inventory.append("Holo-Drive")
    slipdrive_room()

def option_conductingwire():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("Out of options you return to the power room, and subdue the Chosen,")
    print("you use the wrap to bind her, this rabid behavior doesn't make sense, you remove her ID card.")
    slipdrive_room()
    

def slipdrive_room():
    print(" ")
    print("You continue moving, you can hear the rumbling of the Slip Drive up ahead")
    print("Power hums around the large cavernous room, you can see:")
    time.sleep(1)
    slipdrive_choice()

def slipdrive_choice():
    print(" ")
    print("A. an automated terminal")
    print("B. the transport tube to bridge navigation")
    print("C. an exit to the left leading to the Hibernation Core")
    print("D. an exit to the right leading to the Medical facilities.")
    print(" ")
    print("Where do you want to go from the Slip Drive? [A/B/C/D]")
    choice = input(">>> ")
    if choice in answer_a:
        option_terminal()
    elif choice in answer_b:
        option_transporttube()
    elif choice in answer_c:
        option_hibernation()
    elif choice in answer_d:
        option_medical()
    else:
        print("You must choose an option")
        slipdrive_choice()
    
def option_terminal():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print('                                           -----')
    print('                                              /      \ ')
    print('                                              )      |')
    print('       :================:                      "    )/')
    print('      /||              ||                      )_ /*')
    print('     / ||  Enter Code  ||                          *')
    print('    |  ||              ||                   (=====~*~======)')
    print('     \ ||              ||                  0      \ /       0')
    print('       ==================                //   (====*====)   ||')
    print('........... /      \.............       //         *         ||')
    print(':\        ############            \    ||    (=====*======)  ||')
    print(': ---------------------------------     V          *          V')
    print(': |  *   |__________|| ::::::::::  |    o   (======*=======) o')
    print('\ |      |          ||   .......   |    \\         *         ||')
    print('  --------------------------------- 8   ||   (=====*======)  //')
    print('                                     8   V         *         V')
    print('  --------------------------------- 8   =|=;  (==/ * \==)   =|=')
    print('  \   ###########################  \   / ! \     _ * __    / | \ ')
    print('   \  +++++++++++++++++++++++++++   \  ! !  !  (__/ \__)  !  !  !')
    print('    \ ++++++++++++++++++++++++++++   \        0 \ \V/ / 0')
    print('     \________________________________\     ()   \o o/   ()')
    print('      *********************************     ()           () ')
    time.sleep(2)
    print(" ")
    print("You see a message repeating on the terminal")
    time.sleep(0.5)
    print(" ")
    delay_print("This terminal controls the transport tube\n")
    time.sleep(0.5)
    delay_print("You have one more attempt to enter code unauthorised user")
    terminal_choice()

def terminal_choice():
    print(" ")
    print("What would you like to do? [A/B]")
    print(" ")
    print("A. enter the code")
    print("B. Return to the Slip Drive")
    choice = input(">>> ")
    if choice in answer_a:
        doorcode_check()
    elif choice in answer_b:
        slipdrive_choice()
    else:
        print("You must choose an option")
        terminal_choice()

#this is the part that moves onto the final section
def doorcode_check():
    print(" ")
    print(" ")
    print(" ")
    print("Enter code:")
    code = input(">>> ")
    if code in door_code:
        bridge_room()
    else:
        print(" ")
        print(" ")
        print(" ")
        print("The terminal display goes red and sends a destructive wave through your system")
        print("I guess that wasn't the right code after all.")
        death_screen()

def option_transporttube():
    print(" ")
    print(" ")
    print(" ")
    print("You approach the oval transport tube entrance,")
    print("without the terminal activated it is sealed")
    tube_choice()

def tube_choice():
    print(" ")
    print("What would you like to do? [A/B]")
    print(" ")
    print("A. return to the Slip Drive to find the code")
    print("B. try to open the door with force")
    choice = input(">>> ")
    if choice in answer_a:
        slipdrive_choice()
    elif choice in answer_b:
        print(" ")
        print(" ")
        print(" ")
        print("You grip each side of the entrance door, despite your low power its forces open...")
        print("the empty tube is open to space!")
        print("You reflect on your choice as you are spat out into the void")
        death_screen()
    else:
        print("You must choose an option")
        tube_choice()
        
    

def option_hibernation():
    print(" ")
    print(" ")
    print(" ")
    print("As you advance down the steps you are met with a stench you can't describe,")
    print("you move further in and discover various damaged pods have already opened,")
    print("embryonic fluid soaks the floor.")
    print(" ")
    print("The room reacts to your presence and as it illuminates you can now see a corpse next to a Power Shard dispenser.")
    hibernation_choice()

def hibernation_choice():
    print(" ")
    print("What do you do? [A/B/C]")
    print("A. inspect the rotten Chosen corpse")
    print("B. inspect the Power Shard Dispenser")
    print("C. return to the Slip Drive")
    choice = input(">>> ")
    if choice in answer_a:
        corpse_choice()
    elif choice in answer_b:
        shard_choice()
    elif choice in answer_c:
        slipdrive_room()
    else:
        print("You must choose an option")
        hibernation_choice()

def corpse_choice():
    print(" ")
    print(" ")
    print(" ")
    print("This has been here for some time, you have discovered the source of the stench.")
    print("His ID badge is missing, his attire implies he was the resident doctor on board")
    print("He looks to have been beaten to death unlike the others, perhaps one of the earliest victims")
    hibernation_choice()
    

def shard_choice():
    if "Holo-Drive" in inventory:
        yes_holo()
    else:
        no_holo()

def yes_holo():
    print(" ")
    print("To your surprise it lights up and you receive a working power shard,")
    print("There's a slot on the back which is the perfect size for the Holo-Drive")
    yes_holo_choice()
    
def yes_holo_choice():
    print(" ")
    print("What would you like to do? [A/B/C]")
    print("A. Use the Power Shard on yourself")
    print("B. Insert the Holo-Drive")
    print("C. return to the Slip Drive")
    choice = input(">>> ")
    if choice in answer_a:
        print(" ")
        print("You are now fully powered but it hasn't really changed your situation")
        print("The Power Shard is still faintly glowing, you may be able to use it one more time")
        yes_holo_choice()
    elif choice in answer_b:
        print(" ")
        print(" ")
        print(" ")
        print("The Holo-drive flickers and buzzes as you insert the Power Shard.")
        print("A faint blue light shimmers and flexes into existence, faceless and without form the holo-drive begins it's pre-recorded message.")
        print(" ")
        delay_print("I am Nexus unit 3...emergency protocols activated, ship in danger...\n")
        delay_print("...unforeseen course change...\n")
        delay_print("...damage to ship extensive....\n")
        delay_print("...unable to reach bridge and reset navigation...\n")
        delay_print("...pods opening out of sequence...\n")
        delay_print("...it's too early...\n")
        delay_print("...medical units destroyed...\n")
        delay_print("...I can hear them coming....\n")
        delay_print("...error!!*%$'...\n")
        delay_print("...I am afraid...\n")
        print("The message ends with a squelch and screams of the Drug Induced Chosen...")
        delay_print("I must reach the bridge\n")
        print(" ")
        print("There may be salvation in the bridge, through the transport tube")
        slipdrive_room()
    elif choice in answer_c:
        slipdrive_room()
    else:
        print("You must choose an option")
        yes_holo_choice()

def no_holo():
    print(" ")
    print(" ")
    print(" ")
    print("To your surprise it lights up and you receive a working power shard,")
    print("There's a slot on the back which looks like it could fit a device, perhaps a Holo-Drive")
    no_holo_choice()
    
def no_holo_choice():
    print(" ")
    print("What would you like to do? [A/B]")
    print("A. Use the Power Shard on yourself")
    print("B. return to the Slip Drive")
    choice = input(">>> ")
    if choice in answer_a:
        print(" ")
        print(" ")
        print(" ")
        print("You are now fully powered but it hasn't really changed your situation")
        print("This could work if you had the Holo-Drive")
        slipdrive_room()
    elif choice in answer_b:
        slipdrive_room()
    else:
        print("You must choose an option")
        no_holo_choice()
        

def option_medical():
    print(" ")
    print(" ")
    print(" ")
    print("You enter the Medical Facilities used for the recovery of Chosen occupants,")
    print("A normally sterile and ordered area is littered with empty Boost Packets,")
    print("The Boost Packet storage door has been forced opened,")
    print("Walking forward you have the following choices:")
    time.sleep(1)
    medical_choice()

def medical_choice():
    print("")
    print("A. Inspect the empty boost packets")
    print("B. Approach the storage door")
    print("C. Bloody markings across the wall")
    print("D. Return to Slip Drive Room")
    print(" ")
    print("What do you want to look at? [A/B/C/D]")
    choice = input(">>> ")
    if choice in answer_a:
        print(" ")
        print(" ")
        print(" ")
        print("These are used by recovering Chosen,")
        print("a dangerous bio-mix it states clearly only take once. Psychosis Warning,")
        print("The entire 10 year stock has been taken, savagely torn apart as if a herd of wild animals came through here.")
        print("This explains the crazy behaviour.")
        medical_choice()
    elif choice in answer_b:
        fight_choice()
    elif choice in answer_c:
        print(" ")
        print(" ")
        print(" ")
        print("Glistening in the light you can make out a message,")
        print("in desperation, somebody has etched,:")
        time.sleep(1)
        print('" 1 9 7 6 "  - SAVE US')
        print("across the wall using a bloody mixture ....is that a finger nail?...,")
        print("The code may activate the terminal")
        medical_choice()
    elif choice in answer_d:
        print(" ")
        print(" ")
        print(" ")
        print("You return to the Slip Drive room,:")
        slipdrive_room()
    else:
        print("You must choose an option")
        medical_choice()

def fight_choice():
    if "Fight" in inventory:
        print(" ")
        print("You can hear the body still twitching, probably safe to avoid it")
        time.sleep(1)
        medical_choice()
    else:
        option_storage()
        
def option_storage():
    print(" ")
    print(" ")
    print(" ")
    print("As you look in the door you are pushed to one side as a crazed Chosen rushes past,")
    print("wild eyed and foaming at the mouth; he circles you")
    storage_choice()
    
def storage_choice():
    time.sleep(1)
    print(" ")
    print("What do you do? [A/B/C]")
    print("A. Activate the medical protocol")
    print("B. Activate defence protocol")
    print("C. Escape")
    choice = input(">>> ")
    if choice in answer_a:
        print(" ")
        print(" ")
        print(" ")
        print("Too crazed to understand he repays your kindness by jamming a sharp medical instrument into your face")
        death_screen()
    elif choice in answer_b:
        fight_scene()
    elif choice in answer_c:
        inventory.append("Fight")
        print(" ")
        print(" ")
        print(" ")
        print ("You run past the Chosen and watch as he haplessly slips on a packet on the floor")
        print("He stumbles forward before slamming face first into a nearby medical cabinet")
        print("You don't bother to check him before you slip back into the medical facility")
        print("")
        time.sleep(1.5)
        medical_choice()
    else:
        print("You must choose an option")
        storage_choice()

        
def fight_scene():
    inventory.append("Fight")
    roll = random.randint(1,30)
    if roll <11:
        time.sleep(1)
        print(" ")
        print(" ")
        print(" ")
        print("You attempt to subdue the crazed Chosen but he overpowers you easily,")
        print("He lets out a piercing scream as he bashes your skull in with a microscope")
        death_screen()
    elif roll>19:
        time.sleep(1)
        print(" ")
        print(" ")
        print(" ")
        print("You managed to wrestle the crazed Chosen to the ground, binding him with anything nearby that can help")
        print("Happy that he's held safely you return to the Medical Bay")
        medical_choice()
    else:
        crazed_roll()
        
def crazed_roll():
    print(" ")
    print("He lunges towards you!")
    roll = random.randint(1,6)
    if roll <4:
        print(" ")
        print(" ")
        print(" ")
        print("You manage to get the crazed Chosen to the ground, but he's stronger than you think")
        print("")
        print("He swings wildly, landing the scalpel straight into your eye socket, everything goes black")
        death_screen()
    else:
        print(" ")
        print(" ")
        print(" ")
        print("The crazed Chosen manages to swipe at you, drawing blood, but ultimately losing his grip")
        print("In his anger he throws himself at you, landing on nearby equipment and impaling himself")
        print("")
        time.sleep(1)
        print("Clearly the boost packets don't improve your intelligence")
        print("Finally safe you can return to the medical facilities")
        medical_choice()



def bridge_room():
    print(" ")
    print(" ")
    print(" ")
    print("Finally you arrive in the bridge, the view around you is chaotic but the lack of movement makes you feel a little safer")
    print("The floor is strewn with bodies, some of these seem to still have their ID badges.")
    time.sleep(1)
    print(" ")
    print("A small blinking light from a terminal up ahead catches your eye, you could use that to check for nearby planets")
    print("It'll need a password though")
    time.sleep(1)
    print("There's a few broken cabinets laying nearby, documents littering the floor nearby")
    time.sleep(1)
    print("Finally you spot them, survivors within the security bay, locked at the back")
    print("You are their only hope")
    bridge_choice()

def bridge_choice():
    print("")
    print("What do you do? [A/B/C]")
    print("A. inspect bodies")
    print("B. inspect the cabinets")
    print("C. inspect terminal")
    choice = input(">>> ")
    if choice in answer_a:
        print(" ")
        print(" ")
        print(" ")
        print("You check some of the ID badges, a slight sadness coming over you as you begin to recognise a few names")
        time.sleep(1)
        print(" ")
        print("One in particular stands out, Jeff from the tech department, he was always complaining about the lack of security")
        print("The terminals were easy to crack because of a terrible password system, only 6 letters, always a word")
        print("It even let you just guess like it's giving you clues")
        print("")
        time.sleep(1)
        print("Maybe the password will be easier to work out than you thought")
        bridge_choice()
    elif choice in answer_b:
        print("")
        print(" ")
        print(" ")
        print("Most of the paperwork seems useless, invoices, stock checks, all the basics")
        print("One of the memos stands out, another one of Jeffs rants")
        print(" ")
        time.sleep(1)
        print("STOP SETTING PASSWORDS THAT ARE TOO EASY, FAVOURITE ANIMALS ARE TOO OBVIOUS!!!")
        time.sleep(2)
        print("Jeff always was useful")
        bridge_choice()
    elif choice in answer_c:
        final_terminal()
    else:
        print("You must choose an option")
        bridge_choice()


def final_terminal():
    print('                      /                                                    \ ')
    print('                     |    _____________________________________________     | ')
    print('                     |   |                                             |    | ')
    print('                     |   |  C:\> _    SHIPS BRIDGE CONTROL             |    | ')
    print('                     |   |  ENTER PASSWORD                             |    | ')
    print('                     |   |                                             |    | ')
    print('                     |   |                                             |    | ')
    print('                     |   |                                             |    | ')
    print('                     |   |                                             |    | ')
    print('                     |   |                                             |    | ')
    print('                     |   |                                             |    | ')
    print('                     |   |                                             |    | ')
    print('                     |   |                                             |    | ')
    print('                     |   |                                             |    | ')
    print('                     |   |                                             |    | ')
    print('                     |   |_____________________________________________|    | ')
    print('                     |                                                      | ')
    print('                      \_____________________________________________________/ ')
    print('                             \_______________________________________/ ')
    print('                          _______________________________________________ ')
    print('                       _-`    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_ ')
    print('                    _-`.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_ ')
    print('                 _-`.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_ ')
    print('              _-`.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_ ')
    print('           _-`.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_ ')
    print('          :-----------------------------------------------------------------------------: ')
    print('          `---._.-----------------------------------------------------------------._.---` ')
             
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("The only text on the screen shows 'ENTER PASSWORD'")
    print("There's 10 chances left remaining on guessing the password")
    print("You have to enter 1 character at a time")
    print("")
    time.sleep(1)
    print("Do you want to attempt the password? [Y/N]")
    choice = input(">>> ")
    if choice in yes:
        password_game()
    elif choice in no:
        bridge_choice()
    else:
        print("You must choose an option")
        final_terminal()

def password_game():
    print(" ")
    print("Enter First Character...")
    time.sleep(0.5)
    hangman("rabbit")


def hangman(word):
    guesses = " "
    turns = 10
    while turns > 0:
        failed = 0         
        for char in word:      
            if char in guesses:    
                print (char),    
            else:
                print ("_"),     
                failed += 1    

        if failed == 0:
            print("")
            print("You hear the sound of the engine rumble into action, the ship is turning")
            print("A message on the terminal an SOS beacon is back online,")
            print("a nearby planet with hope of salvation is on the radar")
            print("You're saved!")
            print(" ")
            print(" ")
            print ('                                 ___________')
            print ('                             .---`::`        `---.')
            print ('                            (::::::`              )')
            print ('                            |`-----._______.-----`|')
            print ('                            |              :::::::|')
            print ('                           .|               ::::::!-')
            print ('                           \|               :::::/|/')
            print ('                            |               ::::::|')
            print ('                            |   Congratulations! :|')
            print ('                            |                 ::::|')
            print ('                            |               ::::::|')
            print ('                            |              .::::::|')
            print ('                            J              :::::::F')
            print ('                             \            :::::::/')
            print ('                              `.        .:::::::`')
            print ('                                `-._  .::::::-`')
            print ('____________________________________|  """|"_________________________________________')
            print ('                                    |  :::|')
            print ('                                    F   ::J')
            print ('                                   /     ::\ ')                                       
            print ('                              __.-`      :::`-._')
            print ('                             (_           ::::::_)')
            print ('                               `"""---------"""`')
            start_again()
            break

        guess = input(">>>") 
        guesses += guess                    
        if guess not in word:  
            turns -= 1        
            print ("INCORRECT")    
     
            print ("You have", + turns, 'more attempts' )
     
            if turns == 0:
                print(" ")
                print("The screen turns red, sirens scream around you")
                print("INCORRECT PASSWORD - FAILED ATTEMPTS EXCEEDS LIMIT")
                print("A power surge rushes through your body")
                death_screen()
    


def death_screen():
    time.sleep(1)
    print(" ")
    print(" ")
    print('          @@@@@                                        @@@@@')
    print('         @@@@@@@                                      @@@@@@@')
    print('         @@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@')
    print('          @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@')
    print('              @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@')
    print('                @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@')
    print('                  @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@')
    print('                     @@@@@@@    @@@@@@    @@@@@@')
    print('                     @@@@@@      @@@@      @@@@@')
    print('                     @@@@@@      @@@@      @@@@@')
    print('                      @@@@@@    @@@@@@    @@@@@')
    print('                       @@@@@@@@@@@  @@@@@@@@@@')
    print('                        @@@@@@@@@@  @@@@@@@@@')
    print('                    @@   @@@@@@@@@@@@@@@@@   @@')
    print('                    @@@@  @@@@ @ @ @ @ @@@@  @@@@')
    print('                   @@@@@   @@@ @ @ @ @ @@@   @@@@@')
    print('                 @@@@@      @@@@@@@@@@@@@      @@@@@')
    print('               @@@@          @@@@@@@@@@@          @@@@')
    print('            @@@@@              @@@@@@@              @@@@@')
    print('           @@@@@@@                                 @@@@@@@')
    print('            @@@@@                                   @@@@@')
    print(" ")
    print('         *********************************************************')
    print('         *****                   YOU DIED                    *****')
    print('         *********************************************************')

    time.sleep(2)
    if "Holo-Drive" or "Fight" in inventory:
        del inventory[:]
        start_again()
    else:
        start_again()

def start_again():
    print("\n Would you like to try again? Y/N")
    choice = input(">>> ")
    if choice in yes:
        title()
    elif choice in no:
        print("Goodbye")
    else:
        print("You must choose an option")
        start_again()
        


        
title()

