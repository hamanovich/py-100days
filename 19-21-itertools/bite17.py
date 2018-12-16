import itertools

friends = 'Bob Dante Julian Martin'.split()


def friends_teams(friends=friends, team_size=2, order_does_matter=False):
    # if order_does_matter:
    #     team = list(itertools.permutations(friends, team_size))
    # else:
    #     team = list(itertools.combinations(friends, team_size))
    if order_does_matter:
        team = itertools.permutations
    else:
        team = itertools.combinations

    return team(friends, team_size)


if __name__ == "__main__":
    print(list(friends_teams()))
    print(list(friends_teams(order_does_matter=True)))
