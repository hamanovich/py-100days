NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names=NAMES):
    """Should return a list of names, each name appears only once"""
    return list(set([name.title() for name in names]))
    # return list({name.title() for name in names})


dedup_and_title_case_names()


def sort_by_surname_desc(names=NAMES):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names,
                  key=lambda name: name.split()[1],
                  reverse=True)


sort_by_surname_desc()


def shortest_first_name(names=NAMES):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    names = [name.split()[0] for name in names]
    return min(names, key=len)
    # return sorted(names, key=lambda name: len(name.split()[0]))[0].split()[0]


shortest_first_name()
