from functools import wraps


def make_html(element):
    def decorator(func):
        @wraps(func)
        def wrapper():
            return str(f'<{element}>{func()}</{element}>')
        return wrapper
    return decorator


@make_html('section')
@make_html('p')
@make_html('strong')
def get_text(text='I code with Python'):
    return text

print(get_text())
# <p><strong>I code with PyBites</strong></p>
