import random
import csv

from Player import Player

import constants

RULES = {}


def main():
    print_header()
    read_table()
    game_loop(Player.create(), Player.create())


def print_header():
    print('Rock, Paper or Scissors!')
    print('========================')
    print()


def game_loop(player, computer):
    while max(player.score, computer.score) != constants.ROUND:
        cmd_player = input(
            f'What do you choose, {player}: rock, scissors or paper? ').lower()
        cmd_computer = computer.go()

        if cmd_player not in RULES.keys():
            print('You typed wrong command. Try again')
            continue

        print(f'{computer.name} chosen `{cmd_computer}`')

        if cmd_player == cmd_computer:
            print(f'{cmd_player} vs {cmd_computer} = Draw!')
        elif RULES[cmd_computer][cmd_player]:
            computer.scored()
            print(f'{computer.name} has won')
        else:
            player.scored()
            print('You won! Gratz!!!')

        print(f'{player.score} vs. {computer.score}')

        rewarding(player, computer)


def rewarding(player, computer):
    if player.score == constants.ROUND or computer.score == constants.ROUND:
        if player.score == constants.ROUND:
            print(
                f'{player.name} has won. The final score is {player.score}:{computer.score}')
        else:
            print(
                f'{computer.name} has won. The final score is {player.score}:{computer.score}')


def read_table():
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            read_row(row)


def read_row(row):
    name = row['Attacker']

    del row['Attacker']
    del row[name]

    name = name.lower()

    for k in row.keys():
        can_defeat = row[k].strip().lower() == 'win'
        if name not in RULES:
            RULES[name] = {}

        RULES[name][k.lower()] = can_defeat

    return RULES


if __name__ == "__main__":
    main()
