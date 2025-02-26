import random
import csv

# TODO: RANDOM GENERATOR FUNCTION

def random_motion():
    with open('random-motions.csv', 'r') as f:
        motion_set = csv.reader(f)
        motion_set = list(motion_set)
        motion_num = random.randint(1, len(motion_set))

        print('\033[1m' + f'\nMotion: {motion_set[motion_num][0]}\n' + '\033[0m')
        if motion_set[motion_num] is not None:
            print(f'Infoslide:{motion_set[motion_num][1].replace("|", ",")}\n')
        print(f'Tournament:{motion_set[motion_num][2]}\n')
        print(f'Round:{motion_set[motion_num][3]}\n')
        
        return 0
    

# TODO: SEARCH MOTION FUNCTION


# TODO: FILTER BY TOURNAMENT FUNCTION
def search_by_tournament(tournament_name):
    with open('random-motions.csv', 'r') as f:
        motion_set = csv.reader(f)
        motion_set = list(motion_set)
        for i in range(len(motion_set)):
            if  "".join(tournament_name.lower().split()) in "".join(motion_set[i][2].lower().split()):
                print(f'Tournament: {motion_set[i][2]}')
                print('\033[1m' + f'\nRound{motion_set[i][3]}: {motion_set[i][0]}\n' + '\033[0m')
            
        return 0

# TODO: MAIN MENU
def main():
    print("Welcome to the Random Motion Generator!")
    print("""Select an option to begin:
          1. Random Motion Generator
          2. Search for Motion
          3. Theme Selection\n""")
    option = input("> ")
    if option.lower().strip() in ["1", "one"]:
       random_motion()
    elif option.lower().strip() in ["2", "two"]:
        tournament_name = "".join(input("Tournament Name: ").lower().split())
        search_by_tournament(tournament_name)

if __name__ == "__main__":
    main()
