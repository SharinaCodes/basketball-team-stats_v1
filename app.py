import constants as const
import sys
from statistics import mean

players = const.PLAYERS.copy()
teams = const.TEAMS.copy()
clean_players = []

def show_stats():
    print("A) Panthers")
    print("B) Bandits")
    print("C) Warriors")

    option = input("\nEnter an option: ").upper()
    
    if option == 'A':
        team = balanced_teams['Panthers']
        print("\nTeam Panther Stats")
        print("--------------------")
    elif option == 'B':
        team = balanced_teams['Bandits']
        print("\nTeam Bandits Stats")
        print("--------------------")
    elif option == 'C':
        team = balanced_teams['Warriors']
        print("\nTeam Warriors Stats")
        print("--------------------")

    # parse data for summary
    experienced = []
    inexperienced = []
    sum_heights = 0
    team_players = []
    team_guardians = []

    for player in team:
        if player['experience'] is True:
            experienced.append(player)
        else:
            inexperienced.append(player)
        sum_heights += player['height']
        team_players.append(player['name'])
        #flatten list of lists
        team_guardians.extend(player['guardians'])

    avg_height = sum_heights / len(team)
    
        
    print(f"Total players: {len(team)}")
    print(f"Total experienced: {len(experienced)}")
    print(f"Total inexperienced: {len(inexperienced)}")
    print(f"Average height: {avg_height: .2f}")
    print("\nPlayers on Team:")
    print(" ", ", ".join(team_players))
    print("\nGuardians:")
    print(" ", ", ".join(team_guardians))

    print("\nPress ENTER to continue...")
    

def show_menu():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("---- MENU----\n")
    print("Here are your choices:")
    print(" A) Display Team Stats")
    print(" B) Quit\n")

    option = input("Enter an option: ").upper()

    if option == 'B':
        sys.exit()
    else:
        show_stats()

def balance_teams():
    balanced_teams = {}

    #initialize teams
    for i in range(len(teams)):
        balanced_teams[teams[i]] = []

    for i, player in enumerate(clean_players):
        # round robin
        team = teams[i % len(teams)]
        balanced_teams[team].append(clean_players[i])

    return balanced_teams

def height_to_int(height):
    strip_height = height.split(' ')
    return int(strip_height[0])

def exp_to_boolean(experience):
    if experience.upper() == 'YES':
        return True
    return False

def split_guardians(guardians):
    return guardians.split(' and ')


if __name__ == '__main__':
    for player in players:
        height = height_to_int(player['height'])
        experience = exp_to_boolean(player['experience'])
        guardians = split_guardians(player['guardians'])

        clean_player = {'name': player['name'], 'guardians': guardians, 'experience': experience, 'height': height}

        clean_players.append(clean_player)

    balanced_teams = balance_teams()
    show_menu()