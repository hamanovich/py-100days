import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]
# ('Tim', 'DE', False)
# ('Bob', 'ES', True)
# ('Julian', 'AUS', True)
# ('Carmen', 'NL', False)
# ('Sofia', 'BR', True)
# ('Mike', 'US', '-')
# ('Kim', '-', '-')
# ('Andre', '-', '-')


def get_attendees():
    for i, name in enumerate(names):
        loc = locations[i] if i < len(locations) else '-'
        conf = confirmed[i] if i < len(confirmed) else '-'
        print((name, loc, conf))

def get_attendees_zip():
    for participant in itertools.zip_longest(names, locations, confirmed, fillvalue='-'):
        print(participant)

get_attendees_zip()


if __name__ == '__main__':
    get_attendees()