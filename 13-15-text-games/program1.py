import random

from Player import Player

import constants

def main():
    print_header()
    player, computer = get_players_name()
    game_loop(player, computer)


def print_header():
    print('Rock, Paper or Scissors!')
    print('========================')
    print()

def get_players_name():
    player = Player.create()
    computer = Player.create()
    return player, computer

def game_loop(player, computer):
    while max(player.score, computer.score) != constants.ROUND:
        cmd_player = input(f'What do you choose, {player}: rock, scissors or paper? ').lower()
        cmd_computer = computer.go()        
    
        if cmd_player not in constants.CHOICES:
            print('You typed wrong command. Try again')
            continue

        print(f'{computer.name} chosen {cmd_computer}')

        if cmd_player in constants.RULES[cmd_computer]:
            computer.scored()
            print(f'{computer.name} has won')
        elif cmd_player == cmd_computer:
            print(f'{cmd_player} vs {cmd_computer} = Draw!')
        else:
            player.scored()
            print('You won! Gratz!!!')

        print(f'{player.score} vs {computer.score}')

        rewarding(player, computer)

        
def rewarding(player, computer):
    if player.score != constants.ROUND or computer.score != constants.ROUND:
        if player.score == constants.ROUND:
            print(f'{player.name} has won. The final score is {player.score}:{computer.score}')
        else:
            print(f'{computer.name} has won. The final score is {player.score}:{computer.score}')


if __name__ == "__main__":
    main()
