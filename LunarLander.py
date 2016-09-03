# game constants
StartingAltitude = 1000.0
StartingVelocity = 0.0
StartingFuel = 1000.0
CrashSpeed = -10
Gravity = 1.6
ForcePerFuel = 0.15


def initialize_lander():
    global CurrentAltitude
    global CurrentVelocity
    global CurrentFuel
    CurrentAltitude = StartingAltitude
    CurrentVelocity = StartingVelocity
    CurrentFuel = StartingFuel
    return

def restart():
    play_again = input("Play Again?")
    if(play_again[0] == "y"):
        start_game()
    elif(play_again[0] != "n"):
        restart()
    return

def crash():
    print("Oh no! You have Crashed. You have left a crater ", CurrentAltitude - CurrentVelocity, " meters deep")
    restart()
    return

def land():
    print("You breath a sigh of relief. You've landed safely.\nCongratulations you have landed on the lune.")
    print("You emerge from your capsule and explore the surface, you burst with joy as you're finally freed")
    print("from the oppresive shackles of the Earth's gravity. You leap from crater to crater amazed ...\nit feels like flying")
    print("... first it starts with thousands of pinpoint sized glowing red eyes staring at you from the moon caves.")
    print("but rapidly and before you can react a million beasts skitter and emerge from moon caverns, below the surface")
    print("Sadly, you were unaware of the giant space rats inhabiting the planet ")
    print("There is no cheese here, only the flesh of hapless space chumps like you")
    print("you have enough time for one final thought as they devour you whole: 'is this winning?'")
    restart()
    return

def check_landing():
    global CurrentAltitude
    CurrentAltitude = CurrentAltitude + CurrentVelocity
    if(CurrentAltitude <= 0):
        if(CurrentVelocity <= CrashSpeed):
            crash()
        else:
            land()
    main_loop()
    return

def process_gravity(upward_force):
    global CurrentVelocity
    CurrentVelocity = CurrentVelocity - Gravity + upward_force
    check_landing()
    return

def report_lander_status():
    print("The lander is currently at an altitude of: ", CurrentAltitude)
    print("You are travelling at a rate of: ", CurrentVelocity)
    print("You have ", CurrentFuel, " In reserve")
    return

def request_user_action():
    fuel_burn = float(input("How much fuel would you like to burn? Enter a number: "))

    if(fuel_burn > CurrentFuel):
        fuel_burn = CurrentFuel
    elif (fuel_burn < 0):
        fuel_burn = 0
    global CurrentFuel
    CurrentFuel = CurrentFuel - fuel_burn
    return fuel_burn * ForcePerFuel

def main_loop():
    report_lander_status()
    upward_force = request_user_action()
    print("upward_force", upward_force)
    process_gravity(upward_force)
    return

def start_game():
    initialize_lander()
    main_loop()
    return

start_game()