# game constants
StartingAltitude = 1000.0
StartingVelocity = 0.0
Gravity = 1.6
StartingFuel = 1000.0
ForcePerFuel = 0.15


def initialize_lander():
    global CurrentAltitude
    global CurrentVelocity
    global CurrentFuel
    CurrentAltitude = StartingAltitude
    CurrentVelocity = StartingVelocity
    CurrentFuel = StartingFuel
    return

def get_input():

    return

def process_time():

    return

def report_lander_status():
    print("The lander is currently at an altitude of: ", CurrentAltitude)
    print("You are travelling at a rate of: ", CurrentVelocity)
    print("You have ", CurrentFuel, " In reserve")
    return

def request_user_action():
    fuel_burn = raw_input("How much fuel would you like to burn? Enter a number: ")
    return


def main_loop():
    report_lander_status()

    # is the game running?
    #   - yes
    #   - no
    # can we end the round?
    return

def start_game():
    initialize_lander()
    main_loop()
    return

start_game()