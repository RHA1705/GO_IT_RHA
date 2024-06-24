from functools import wraps


def greeting(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('hello')
        result = func(*args, **kwargs)
        return result

    return wrapper


@greeting
def person(name: str):
    """
    Print person's name
    """
    print(name)


if __name__ == '__main__':
    person('John')
    print(person.__name__)
    print(person.__doc__)
    print(person.__annotations__)
