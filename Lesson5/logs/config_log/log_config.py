import logging, os

def init_log(name):    #Создаем функцию экземпляр логгера
    client_log = logging.getLogger(name)
    client_log.setLevel(logging.INFO)

    #Создаем обработчик
    CLIENT_LOG_CONFIG_FOLDER_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    CLIENT_LOG_FILE_PATH = os.path.join(CLIENT_LOG_CONFIG_FOLDER_PATH, f'{name}.log')
    file_hand = logging.FileHandler(CLIENT_LOG_FILE_PATH,encoding='utf-8')
    file_hand.setLevel(logging.INFO)
    #Определяем формат лога
    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s: %(funcName)s - %(message)s ")

    #Добавляем формат к обработчику
    file_hand.setFormatter(log_format)
    #Добавляем обработчик логгеру
    client_log.addHandler(file_hand)
    return logging.getLogger(name)