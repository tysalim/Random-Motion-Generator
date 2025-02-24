import os
import random
import time

# TODO: RANDOM GENERATOR FUNCTION

def random_motion():
    with open('random-motions.csv', 'r') as f:
        motion_set = csv.reader(f)
        motion_set = list(motion_set)
        motion_num = random.randint(1, len(motion_set))
        print(f'Motion: {motion_set[motion_num][0]}\n')
        if motion_set[motion_num] is not None:
            print(f'Infoslide: {motion_set[motion_num][1]}\n')
        print(f'Tournament: {motion_set[motion_num][2]}\n')
        return 0
    

# TODO: SEARCH MOTION FUNCTION

# TODO: FILTER BY TOURNAMENT FUNCTION

# TODO: MAIN MENU
def main():
    print("Welcome to the Random Motion Generator!")
    print("""Select an option to begin:
          1. Random Motion Generator
          2. Search for Motion
          3. Theme Selection""")
    option = input("> ")
    if option.lower().strip() in ["1", "one"]:
       random_motion()

main()
