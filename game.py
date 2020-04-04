import random

def roll_dice(number_of_dice, number_of_faces):
    # Assumes number_of_faces and number_of_dice are already validates
    die_rolls = []

    for _ in range(number_of_dice):
        die_rolls.append(random.randint(1, number_of_faces))

    print("You have rolled:", die_rolls)
    print("These die sum to ", 
          sum(die_rolls), 
          "and an average rounded value of ", 
          round(average(die_rolls)))
    
    return die_rolls

def validateInt( min, max, prompt ):
    # ASSUME min and max are valid positive integers, and that min < max
    if prompt >= min and prompt <= max:
        return True

    return False

def validateStr( prompt, listOfChoices ):
    # assume prompt is a String and listOfChoices is a list of Strings.
    return ""

def average(l):
    # l is a list
    return sum(l)/len(l)

def calculatePercentage( sides, dice, diceRolls ):
    # ASSUME sides*dice != 0, sides, dice are numbers
    # ASSUME diceRolls is a list of numbers
    return 0

def isPrime(number):
    # go from 1 to number - 1
    #   check if our number divided by that number gives remainder zero
    #   if remainder is 0, then it isn't prime
    #   if after dividing by all numbers, the remainder  isn't 0 then it is prime
    for i in range(2, number):
        remainder = number % i 
        if remainder == 0:
            return False
    return True

def pattern1(die_rolls, number_of_faces):
    # ASSUME sides > 0 and dice is a list of integers
    if number_of_faces >= 4:
        # Check if numbers are equal
        if len(set(die_rolls)) == 1: 
            print("Pattern 1 Matched! All die rolls are the same ", die_rolls)
            return 10
    print("Pattern 1 not matched with your roll ", die_rolls, "... some dice are different")
    return 0

def pattern2(die_rolls, number_of_faces):
    maximum_score = len(die_rolls) * number_of_faces
    if maximum_score >= 20:
        sum_of_rolls = sum(die_rolls)
        if isPrime(sum_of_rolls):
            print("Pattern 2 matched!", sum_of_rolls, "is a prime number!")
            return 15

    print("Pattern 2 not matched!")
    return 0

def pattern3(die_rolls):
    if len(die_rolls) >= 5:
        rounded_avg = round(average(die_rolls))
        count = 0
        for i in range(len(die_rolls)):
           if die_rolls[i] >= rounded_avg:
               count += 1    
        if count >= len(die_rolls)/2:
            print("Pattern 3 Matched!")
            return 5
    print("Pattern 3 not matched")
    return 0

def pattern4(die_rolls, number_of_faces):
    if len(die_rolls) > 4 and number_of_faces > len(die_rolls):
        if len(set(die_rolls)) == len(die_rolls):
            print("Pattern 4 matched! All dice have different values!")
            return 8
    print("Pattern 4 Not matched!")
    return 0
    
def bonusFactor(die_rolls, number_of_faces):
    bonus_factor = 0
    bonus_factor += pattern1(die_rolls, number_of_faces)
    bonus_factor += pattern2(die_rolls, number_of_faces)
    bonus_factor += pattern3(die_rolls)
    bonus_factor += pattern4(die_rolls, number_of_faces)

    if bonus_factor == 0:
        print("No patterns matched! You get a bonus factor of 1")
        bonus_factor = 1
    else:
        print("Since bonus factor is ", bonus_factor, "Pattern 5 is not matched")

    return bonus_factor

def score(die_rolls, number_of_faces):
    bonus_factor = bonusFactor(die_rolls, number_of_faces)
    percentage = sum(die_rolls) / (number_of_faces * len(die_rolls))
    
    score = bonus_factor * percentage + (770675%2020)
    return score

def accept_input(min, max, input_name):
    """ Takes input between the range min and max and
        validates it
    """
    #TODO: Fix first time string input error
    if input_name == "faces":
        value = int(input("Enter # of faces[2, 20]: "))
    elif input_name == "dice":
        value = int(input("Enter # of die[3, 6]: "))

    while not validateInt(min, max, value):
        print("Try again!")
        try:
            if input_name == "faces":
                value = int(input("Enter # of faces[2, 20]: "))
            elif input_name == "dice":
                value = int(input("Enter # of die[3, 6]: "))
        except ValueError:
            print("That's Invalid! Try again")
    
    return value
    
# main

# Don't forget a statement of authorship at the top of the file!
print("Welcome!")

number_of_faces = accept_input(2, 20, "faces")
number_of_dice = accept_input(3, 6, "dice")

die_rolls = roll_dice(number_of_dice, number_of_faces)

print(score(die_rolls, number_of_faces))