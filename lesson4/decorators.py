PASSWORD = '12345'


def needs_password(func):
    def wrapper(*args, **kwargs):
        password = input('Insert your password: ')
        if(password == PASSWORD):
            return func(*args, **kwargs)
        else:
            print('Incorrect password. Try again')

    return wrapper

@needs_password
def happy_birthday_to(*args, **kwargs):
    print('Happy birthday to ' + ', '.join(args))


if __name__ == '__main__':
    happy_birthday_to('Hector', 'Pedro')
