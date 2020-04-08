# I, Nidhay Bhatt, student number 000770675, certify that all code submitted is my own work;
# That I have not copied it from any other source.
# I also certify that I have not allowed my work to be copied by others.

import random

def roll_dice(number_of_dice, number_of_faces):
    """ Takes the number of dice and number of faces as input. 
        Rolls that many number of dies and returns a list of the die rolls
    """

    die_rolls = []

    for _ in range(number_of_dice):
        die_rolls.append(random.randint(1, number_of_faces))

    print("You have rolled:", die_rolls)
    print("These die sum to", 
          sum(die_rolls), 
          "and an average rounded value of", 
          round(average(die_rolls)))
    
    return die_rolls

def reroll_die(die_rolls, die_number, number_of_faces):
    """ Takes in the die rolls, die number and number of faces as the inputs
        and rerolls that die and returns the updated die rolls list
    """
    die_rolls[die_number - 1] = random.randint(1, number_of_faces)
    return die_rolls

def validate_int(min, max, prompt):
    """
        Checks whether the prompt (an integer)
        lies within the min and max
    """ 
    if prompt >= min and prompt <= max:
        return True

    return False


def validate_str(response, list_of_choices):
    """ Converts the response to lowecase and checks
        wheter it is in the list of valid choices
    """
    if response.lower() in list_of_choices:
        return True
    return False

def average(l):
    """Takes a list as an input and returns the average of all its elements
    """
    return sum(l)/len(l)

def is_prime(number):
    """ Checks wheter the number is a prime number or not """
    for i in range(2, number):
        remainder = number % i 
        if remainder == 0:
            return False
    return True

def pattern1(die_rolls, number_of_faces):
    """ Checks whether the die rolls match pattern 1.
        Returns a bonus factor of 10 if pattern 1 matches.
    """
    if number_of_faces >= 4:
        # Check if numbers are equal
        if len(set(die_rolls)) == 1: 
            print("Pattern 1 Matched! All die rolls are the same ", die_rolls)
            return 10
    print("Pattern 1 not matched with your roll", die_rolls, "...some dice are different")
    return 0

def pattern2(die_rolls, number_of_faces):
    """ Checks whether the die rolls match pattern 2.
        Returns a bonus factor of 15 if pattern 2 matches.
    """
    maximum_score = len(die_rolls) * number_of_faces
    if maximum_score >= 20:
        sum_of_rolls = sum(die_rolls)
        if is_prime(sum_of_rolls):
            print("Pattern 2 matched!", sum_of_rolls, "is a prime number!")
            return 15

    print("Pattern 2 not matched,", sum(die_rolls), "is not a prime number!")
    return 0

def pattern3(die_rolls):
    """ Checks whether the die rolls match pattern 3.
        Returns a bonus factor of 5 if pattern 3 matches.
    """
    if len(die_rolls) >= 5:
        rounded_avg = round(average(die_rolls))
        count = 0
        for i in range(len(die_rolls)):
           if die_rolls[i] >= rounded_avg:
               count += 1    
        if count >= len(die_rolls)/2:
            print("Pattern 3 Matched!")
            return 5
    print("Pattern 3 does not apply since there are less than 5 dice")
    return 0

def pattern4(die_rolls, number_of_faces):
    """ Checks whether the die rolls match pattern 4.
        Returns a bonus factor of 8 if pattern 4 matches.
    """
    if len(die_rolls) > 4 and number_of_faces > len(die_rolls):
        if len(set(die_rolls)) == len(die_rolls):
            print("Pattern 4 matched! All dice have different values!")
            return 8
    print("Pattern 4 does not apply since there are either <=4 sides or # sides <= # dice")
    return 0
    
def calulate_bonus(die_rolls, number_of_faces):
    """ Calculates the bonus factor by matching all the patterns
    """
    bonus_factor = 0
    bonus_factor += pattern1(die_rolls, number_of_faces)
    bonus_factor += pattern2(die_rolls, number_of_faces)
    bonus_factor += pattern3(die_rolls)
    bonus_factor += pattern4(die_rolls, number_of_faces)

    if bonus_factor == 0:
        print("Since none of the other patterns were matched, pattern 5 is matched!")
        print("Your bonus factor is 1")
        bonus_factor = 1
    else:
        print("Since bonus factor is ", bonus_factor, "Pattern 5 is not matched")

    return bonus_factor

def calulate_score(die_rolls, number_of_faces):
    """ Calculates the score for the round by factoring in
        the bonus score as well as the percentage
    """
    bonus_factor = calulate_bonus(die_rolls, number_of_faces)
    percentage = sum(die_rolls) / (number_of_faces * len(die_rolls))
    
    score = bonus_factor * percentage + (770675%2020)
    return score

def accept_input(min, max, input_name):
    """ Takes input between the range min and max and
        validates it
    """
    if input_name == "faces":
        value = int(input("Enter # of faces[2, 20]: "))
    elif input_name == "dice":
        value = int(input("Enter # of die[3, 6]: "))

    while not validate_int(min, max, value):
        print("Try again!")
        try:
            if input_name == "faces":
                value = int(input("Enter # of faces[2, 20]: "))
            elif input_name == "dice":
                value = int(input("Enter # of die[3, 6]: "))
        except ValueError:
            print("That's Invalid! Try again")
    
    return value
    
    
if __name__ == "__main__":
    print("COMP 10001 - W2020 Final Project by Nidhay Bhatt, Student number 000770675")
    print("Welcome to my dice game, good luck!")
    
    # Game State Measures
    play_game = True
    rounds = 0
    scores = []
    number_of_faces = accept_input(2, 20, "faces")
    number_of_dice = accept_input(3, 6, "dice")


    # Main Game Loop
    while play_game:
        rounds += 1
        die_rolls = roll_dice(number_of_dice, number_of_faces)
        score = calulate_score(die_rolls, number_of_faces)
        scores.append(score)
        print("These dice are worth", score, "points.")

        reroll_response = input("Do you want to reroll any dice? ['yes', 'no']: ")
        while not validate_str(reroll_response, ["yes", "no"]):
            reroll_response = input("I'm sorry, the choices are ['yes', 'no']. Please pick one of them.")
        
        if reroll_response == "yes":
            for i in range(len(die_rolls)):
                current_die = die_rolls[i]
                response = input("Reroll die {}? (was {}) ['y', 'n']: ".format(i+1, current_die))
                while not validate_str(response, ["y", "n"]):
                    response = input("I'm sorry, the choices are ['y', 'n']. Please pick one of them.")
                
                if response == "y":
                    die_rolls = reroll_die(die_rolls, i+1, number_of_faces)
                elif response == "n":
                    response = input("Are you sure? ['yes', 'no']")
                    while not validate_str(response, ["yes", "no"]):
                        response = input("I'm sorry, the choices are ['y', 'n']. Please pick one of them.")

                    if response == "yes":
                        # quit
                        continue
                    elif response == "no":
                        die_rolls = reroll_die(die_rolls, i+1, number_of_faces)

            # calculate new score
            print("You have rolled: ", die_rolls)
            score = calulate_score(die_rolls, number_of_faces)
            scores[-1] = score
            print("Your Score: ", score)

        if rounds > 1:
            minimum = min(scores[:len(scores) - 1])
            maximum = max(scores[:len(scores)-1])

            if score > maximum:
                print("Congrats! Your score for round", rounds, "was the highest of all previous rounds!")
            elif score < minimum:
                print("Oops! Your score for round", rounds, "was the lowest of all previous rounds!")
            else:
                print("You score of", score, "on turn", rounds, "was average compared to other turns today.")

        if rounds == 1:
            print("This was your first turn, let's go again!")

        continue_game = input("Would you like to play another turn? ['y', 'n']? ")
        while not validate_str(continue_game, ["y", "n"]):
            continue_game = input("I'm sorry, the choices are ['y', 'n']. Please pick one of them.")

        if continue_game == "y":
            play_game = True
        elif continue_game == "n":
            print("Thanks for playing!")
            print("You played a total of", rounds, "rounds!")
            print("Your average score was", sum(scores)/rounds)
            play_game = False

        