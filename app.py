import constants as const

players = const.PLAYERS.copy()
teams = const.TEAMS.copy()
clean_players = []

def balance_teams():
    balanced_teams = {}

    #initialize teams
    for i in range(len(teams)):
        balanced_teams[teams[i]] = []

    for i, player in enumerate(clean_players):
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

print(balance_teams())