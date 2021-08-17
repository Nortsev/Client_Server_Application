import time, pickle
from socket import AF_INET, SOCK_STREAM, socket
import config
import argparse


def create_presence_meassage(account_name='Guest'):
    message = {
        config.ACTION: config.PRESENCE,
        config.TIME: time.time(),
        config.USER: {
            config.ACCOUNT_NAME: account_name
        }
    }
    return message


def start_client():
    s = socket(AF_INET, SOCK_STREAM)
    if config.server_address != '0.0.0.0':
        s.connect((config.server_address, config.server_port))
    else:
        s.connect(('localhost', config.server_port))

    message = create_presence_meassage()
    if isinstance(message, dict):
        message = pickle.dumps(message)
    print(f"Отравляю сообщение {message} на сервер")
    s.send(message)
    print("Ожидаем ответ")
    server_response = pickle.loads(s.recv(1024))
    print(f"Ответ с сервера: {server_response}")
    if server_response.get('response') == 200:
        print("Соеденение с сервером установленно")
    else:
        print("Не известная ошибка")
    s.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='JSON instant messaging'
    )

    parser_group = parser.add_argument_group(title='Parameters')
    parser_group.add_argument('-a', '--addr', default=config.server_address, help='IP address')
    parser_group.add_argument('-p', '--port', type=int, default=config.server_port, help='TCP port')
    start_client()
