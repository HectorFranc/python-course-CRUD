clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer'

    }
]


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients

    for i, client in enumerate(clients):
        print('{id} | {name} | {company} | {email} | {position}'.format(
            id=i,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def update_client(client_id, updated_client):
    global clients

    if client_id < len(clients):
        clients[client_id] = updated_client
    else:
        _message_client_not_in_client_list()


def delete_client(client_id):
    global clients

    if client_id < len(clients):
        clients.pop(client_id)
    else:
        _message_client_not_in_client_list()


def search_client(client_name):
    global clients

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('WELCOME TO HECTOR VENTAS'.center(50))
    print('-' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    client_field = None

    while not client_field:
        client_field = input('What is the client {}?'.format(field_name))

    return client_field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }
    return client


def _message_client_not_in_client_list():
    print('Error: Client is not in clients list')


if __name__ == '__main__':
    _print_welcome()
    command = input('>> ')
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')
