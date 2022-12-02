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
    print(f'{start["name"]} has {start["follower_count"]} likes')
    print(f'{chosen["name"]} has {chosen["follower_count"]} likes')
    if start["follower_count"] >= chosen["follower_count"]:
        print(f'{start["name"]} has more than {chosen["name"]}')
        return True
    else:
        print(f'{chosen["name"]} has more than {start["name"]}')
        return False

def check_answer(input, start_data, chosen_data):
    if input == "l":
        if compare(start_data, chosen_data):
            return True
        else:
            return False
    elif input == "h":
        if not compare(start_data, chosen_data):
            return True
        else:
            return False
    else:
        print("please use a usefull input like h or l")


def game_run():
    print(logo)
    score = 0
    runner = True
    chosen_data = random.randint(0, len(data) - 1)
    start_data = data[chosen_data]
    while runner == True:
        print(f'compare {start_data["name"]} ,a {start_data["description"]} ,from {start_data["country"]}')
        print(f"({vs}+\n")
        chosen_data = data[random.randint(0, len(data) - 1)]
        print(f'compare {chosen_data["name"]} ,a {chosen_data["description"]} ,from {chosen_data["country"]} \n')
        my_input = input(f'has {chosen_data["name"]} one higher [h] ore lower [l] instalikes?').lower()

        ##variant 2 with an function
        if check_answer(my_input,start_data,chosen_data):
            print(f'nice one you guessed rioght ')
            score += 1
        elif not check_answer(my_input, start_data, chosen_data):
            print(f'you lose wrong guess')
            runner = False

        start_data = chosen_data
        print("\n################\n")
    print(f"uffff nice effort. your final score is {score}")


game_run()
