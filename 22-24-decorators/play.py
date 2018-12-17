import functools


def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@uppercase
def greeting(text='Hello'):
    name = input('Name? ')
    return f'{text}, {name}'


print(greeting('Welcome'))


def clip_sentence(words):
    origin_words = words

    def decorator(func):
        '''Decorator to clip sentence by words'''
        try:
            words = int(input('Count? '))
        except ValueError:
            words = origin_words
            print(
                f'Count must be only a number. The default value is {origin_words}')

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            kwargs['text'] = ' '.join(kwargs['text'].split()[:words])
            return func(*args, **kwargs)
        return wrapper
    return decorator


@clip_sentence(words=10)
def get_text(text='This is a pen!'):
    return text


print(get_text(text='Big News! We are changing our name to Data Council, we are still the leading global events where the world gathers to explore the future of data. Please follow our new account here: DataCouncilAI'))
