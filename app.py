import constants as const
import sys
import traceback

players = const.PLAYERS.copy()
teams = const.TEAMS.copy()
clean_players = []

def show_team_options():
    print("A) Panthers")
    print("B) Bandits")
    print("C) Warriors")

def show_stats():
    while True:
        show_team_options()
        team_name = ''

        option = input("\nEnter an option: ").strip().upper()
    
        if option == 'A':
            team_name = 'Panthers'
        elif option == 'B':
            team_name = 'Bandits'
        elif option == 'C':
            team_name = 'Warriors'
        else:
            print("\nInvalid selection (chose A, B, or C): " )

        team = balanced_teams[team_name]
        print(type(team))

        print(f"\nTeam {team_name} Stats")
        print("--------------------")

        # parse data for summary        
        team_players = []
        team_guardians = []

        for player in team['players']:
            team_players.append(player['name'])
            #flatten list of lists
            team_guardians.extend(player['guardians'])
        
            
        print(f"Total players: {len(team)}")
        print(f"Total experienced: {team['exp_count']}")
        print(f"Total inexperienced: {team['inexp_count']}")
        print(f"Average height: {team['avg_height']: .2f}")
        print("\nPlayers on Team:")
        print(" ", ", ".join(team_players))
        print("\nGuardians:")
        print(" ", ", ".join(team_guardians))


        to_exit = input("\nPress ENTER to continue...\nPress any other key to exit\n")

        if to_exit == '':
            print()
            show_menu()
        else:
            sys.exit()

    
    

def show_menu():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("---- MENU----\n")
    
    while True:
        print("Here are your choices:")
        print(" A) Display Team Stats")
        print(" B) Quit\n")

        option = input("Enter an option: ").strip().upper()

        if option == 'A':
            show_stats()
        elif option == 'B':
            sys.exit()
        else:
            print("\nInvalid selection")
        
def balance_teams():
    balanced_teams = {}

    # sort experienced vs inexperienced    
    experienced = []
    inexperienced = []

    for player in clean_players:
        if player['experience'] is True:
            experienced.append(player)
        else:
            inexperienced.append(player)
    
    # initialize teams as dicts with "players" list
    for team in teams:
        balanced_teams[team] = {"players": []}

    # distribute experienced players round robin
    for i, player in enumerate(experienced):
        team_index = i % len(teams)
        team_name = teams[team_index]
        balanced_teams[team_name]["players"].append(player)

    # distribute inexperienced players round robin
    for i, player in enumerate(inexperienced):
        team_index = i % len(teams)
        team_name = teams[team_index]
        balanced_teams[team_name]["players"].append(player)

    # sort each team's players by height
    for team_name, team_data in balanced_teams.items():
        team_data["players"] = sorted(team_data["players"], key=lambda p: p["height"])

    # compute analysis for each team
    for team_name, team_data in balanced_teams.items():
        players = team_data["players"]
        exp_count = 0
        inexp_count = 0
        height_total = 0

        for player in players:
            height_total += player["height"]
            if player["experience"] is True:
                exp_count += 1
            else:
                inexp_count += 1

        avg_height = height_total / len(players)

        team_data["exp_count"] = exp_count
        team_data["inexp_count"] = inexp_count
        team_data["avg_height"] = avg_height

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

def clean_data():
    for player in players:
        height = height_to_int(player['height'])
        experience = exp_to_boolean(player['experience'])
        guardians = split_guardians(player['guardians'])

        clean_player = {'name': player['name'], 'guardians': guardians, 'experience': experience, 'height': height}

        clean_players.append(clean_player)

if __name__ == '__main__':
    try:
        clean_data()
        balanced_teams = balance_teams()
        show_menu()
    except KeyboardInterrupt:
        print("\nGoodbye!")       # allows for Ctrl+C
    except SystemExit:
        raise                     # don’t swallow sys.exit()
    except Exception as e:
        print(f"\nUnexpected error: {e}\nExiting safely.")
        traceback.print_exc()