from actors.player import Player


def handle_player_registration(table):
    more_players = True
    while more_players:
        table.players.append(single_player_registration())
        continue_ = input('Would you like to add any additional players (Y/n): ')
        if continue_ != 'Y':
            more_players = False
    return table


def single_player_registration():
    new_player_name = input('Please enter the name of your new player: ')
    init_bank = input('Please enter the initial bank of your new player: ')

    return Player(new_player_name, init_bank)
