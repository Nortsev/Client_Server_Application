'''3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
 Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке
ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с
помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.'''

import yaml

order_dict = {
    "Item": ['list', 'test', 'yaml'],
    "quantity": 2,
    'third_key': {'inner_key1': '10Ѱ', 'inner_key2': '15※', 'inner_key3': '7€'},
}

with open('file.yaml', 'w', encoding='utf-8') as write:
    yaml.dump(order_dict,write,default_flow_style = False, allow_unicode = True)
    print("Запись в yaml файл завершенна")


with open('file.yaml', 'r', encoding='utf-8') as read:
    print("Чтение файла")
    read_yaml = yaml.load(read,Loader=yaml.SafeLoader)
    if order_dict == read_yaml:
        print("Данные совпадают")