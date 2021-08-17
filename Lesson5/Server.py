import config
from socket import socket, AF_INET, SOCK_STREAM
import sys, pickle
import argparse



def check_correct_presence_and_response(presence_message):
    if config.ACTION in presence_message and \
                    presence_message[config.ACTION] == config.PRESENCE and \
                    config.TIME in presence_message and \
            isinstance(presence_message[config.TIME], float):
        return {config.RESPONSE: config.OK}
    else:
        # Иначе шлем код ошибки
        return {config.RESPONSE: config.WRONG_REQUEST, config.ERROR: 'Не верный запрос'}

def start_server():
    s = socket(AF_INET,SOCK_STREAM)
    s.bind((config.server_address,config.server_port))
    s.listen(1)
    print('Готов к приему клиентов! \n')


    while True:
        client, address = s.accept()
        client_message = pickle.loads(client.recv(1024))
        print(f'Принято сообщение от клиента: {client_message}')
        answer = check_correct_presence_and_response(client_message)
        print(f"Приветствуем пользователя {client_message.get('user').get('account_name')}!")
        print('Отправка ответа клиенту:',answer)
        client.send(pickle.dumps(answer))
        client.close

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='JSON instant messaging'
    )

    parser_group = parser.add_argument_group(title='Parameters')
    parser_group.add_argument('-a', '--addr', default=config.server_address, help='IP address')
    parser_group.add_argument('-p', '--port', type=int, default=config.server_port, help='TCP port')
    start_server()