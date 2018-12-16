import string

# ASCII ABC
letters = list(string.ascii_lowercase)[:13]
print(letters)


def simple_gen():
    yield from range(2,12,2)


gen = simple_gen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def opts():
    options = 'red green yellow pink orange blue'.split()
    
    for option in options:
        yield f'Option: {option}'

print(list(opts()))


heroes = ['Aa Bb', 'BB Aa', 'Hh Uu', 'Ee Kk', 'Cc Dd']
print(sorted(heroes, key=lambda name: name.split()[1]))