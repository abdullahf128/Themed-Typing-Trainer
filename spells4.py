"""
CMPUT 174 Lab 5 'Spells4' Program
Typing Trainer With Complex Time-Based Point System Implemented 
Author: Abdullah Faisal
When: October 10, 2022
"""

# import statements
import random
import time


# reads a list of spells from a file and returns a list of spells
def read_spells(filename: str) -> list[str]:
    
    filemode = "r"
    file = open (filename, filemode)
    spells_list = file.readlines()    
    file.close()
    spells = []
    for spell in spells_list:
        separate_spells = spell.find( '/n' )  # separates spells
        spells.append(spell[0:separate_spells])
        
    return spells

 
# returns a random spell from a list of spells, converted to lowercase.
def get_random_spell(spells: list[str]) -> str:

    len_spells = len (spells)
    random_spell = random.randrange(0,len_spells,1)  # picks random spell
    return spells[random_spell].lower()


# prints header
def display_header():
    
    header = '############################################################'
    print(header + '\n' + 'Harry Potter Typing Trainer' + '\n' + header)


# reads and prints instructions from instructions.txt file
def display_instructions():
    
    filename = 'instructions.txt'
    filemode = "r"
    file = open (filename, filemode)
    instructions_list = file.readlines()    
    file.close()
    for instruction in instructions_list:
        separate_instructions = instruction.find( '\n' )  # separates instruction lines
        print(instruction[0:separate_instructions])


# gets the spell as input from the user and returns it.
def get_user_input(spell: str) -> str:
    
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time


# calculates and rounds target typing time for spell to one decimal (returns target typing time)
def get_target_time(spell: str) -> float:
    
    spell_letters = len (spell)
    target_typing_time = round(0.3 * (spell_letters), 1)  # target typing time formula (rounded to one decimal)
    return target_typing_time


# displays feedback (correct or incorrect) to the user
def display_feedback(spell: str, user_input: str):
    
    if spell == user_input:
        print('Correct!')
    else:
        print('Incorrect!' + '\n' + 'The correct spell was: ' + spell)


# asks the user if they want to play again, returns True if the user enters Y or y, False otherwise
def play_again() -> bool:
    
    print('Do you want to practice more? (y/n)')
    bool_input = input('')
    if bool_input == 'Y':
        return True
    elif bool_input == 'y':
        return True
    else:
        return False


# determines points user gets based on time taken to respond and correctness (returns score)
def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    
    score = 0
    if spell == user_input and get_target_time(spell) >= user_time:
        score += 10
    elif spell == user_input and (get_target_time(spell) * 1.5) >= user_time > get_target_time(spell):
        score += 6
    elif spell == user_input and (get_target_time(spell) * 2) >= user_time > (get_target_time(spell) * 1.5):
        score += 3
    elif spell == user_input and user_time > (get_target_time(spell) * 2):
        score += 1        
      
    else:
        score = score - 5
        
    return score


# calls all functions in order to run typing trainer program and prints points/scores
def main() -> None:
    
    again = True
    score = 0
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    
    while again == True:
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        display_feedback(spell, user_input[0])
        points = calculate_points(spell, *user_input)
        score = score + points
        print('You get', points, 'points! Your score is:', score)
        again = play_again()
    print('Your final score is:', score)
            
            

main()