"""2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра."""

import datetime
import json

date = datetime.datetime.now().strftime("%Y-%m-%d - %H.%M")


def write_order_to_json(item, quantity, price, buyer, date):
    order_dict = {
        "Item": item,
        "quantity": quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    with open('orders.json', 'w', encoding='utf-8') as write:
        json.dump({"orders": [order_dict]}, write, indent=4, ensure_ascii=False)
    return print("Запись данных прошла успешно")


if __name__ == "__main__":
    write_order_to_json('Iphone', 5, 49990, 'Ivan Ivanov', date)
