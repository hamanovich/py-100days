import random
import itertools

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def reverse_names(names=NAMES):
    '''
    Reverse the names and title them
    '''
    print([
        ' '.join(reversed(name.split())).title()
        for name in names
    ])


reverse_names()


def random_pairs(names=NAMES):
    '''
    Use generator to take random pairs
    '''
    while True:
        name1, name2 = random.choice(names).split(
        )[0].title(), random.choice(names).split()[0].title()
        yield f'{name1} teams up with {name2}'


pairs = random_pairs()

iterm_pairs = itertools.islice(pairs, 5)
print(list(iterm_pairs))

for _ in range(5):
    print(next(pairs))
