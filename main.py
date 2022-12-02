'''this is my higher lower game'''

from game_data import data
from art import logo
from art import vs
import random
import os

def clear_screen():
    '''this should clear the screen but doesnt work'''
    os.system('cls' if os.name == 'nt' else 'clear')

chosen_data = random.randint(0, len(data) - 1)
start_data = data[chosen_data]
name = start_data["name"]

def compare(start, chosen):
    '''is the first one higher than the second one?  yes =return True no =return False'''
    if start["follower_count"] >= chosen["follower_count"]:
        print(start["follower_count"])
        print(chosen["follower_count"])
        return True
    else:
        print("--")
        return False

def game_run():
    score = 0
    runner = True
    chosen_data = random.randint(0, len(data) - 1)
    start_data = data[chosen_data]
    while runner == True:
        print(f'compare {start_data["name"]} ,a {start_data["description"]} ,from {start_data["country"]}')
        print(f"({vs}+\n")
        chosen_data = data[random.randint(0, len(data) - 1)]
        print(f'compare {chosen_data["name"]} ,a {chosen_data["description"]} ,from {chosen_data["country"]}')
        my_input = input("has the second one higher [h] ore lower [l] likes?")
        if my_input == "l":
            if compare(start_data, chosen_data):
                print(f"nice one {start_data} won against \n {chosen_data} ")
                score += 1
            else:
                print(f"you lose {start_data} won against \n {chosen_data} ")
                runner = False
        if my_input == "h":
            if not compare(start_data, chosen_data):
                print(f"you win because {start_data} loses against \n {chosen_data} ")
                score += 1
            else:
                print(f"you lose {start_data} loses against \n {chosen_data} ")
                runner = False
        start_data = chosen_data
    print(f"uffff nice effort. your final score is {score}")

game_run()
