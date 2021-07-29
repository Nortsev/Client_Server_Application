'''1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
a.
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить
в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить
в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать
получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
c. Проверить работу программы через вызов функции write_to_csv().'''
import os, re, csv


def name_file():
    path_file = []
    for file in os.listdir('data'):
        if file.endswith('.txt'):
            path_file.append(os.path.join('data', file))
    return path_file


def get_data(path_file):
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for path in path_file:
        with open(path, 'r', encoding='windows-1251', ) as file:
            content = file.read()
            os_prod_list = path, re.findall('Изготовитель системы:\s+(\w+)', content)[0].strip()
            os_name_list = path, re.findall('Название ОС:\s+([\w\.\s]+)\n', content)[0].strip()
            os_code_list = path, re.findall('Код продукта:\s+([\w\-]+\w+)', content)[0].strip()
            os_type_list = path, re.findall('Тип системы:\s+([\w\-\w\s\w]+)\n', content)[0].strip()

            main_data.extend([[os_prod_list[1], os_name_list[1], os_code_list[1], os_type_list[1]]])
    return main_data


def create_cvs(data):
    with open("main_data.csv", 'w', encoding='windows-1251') as test_w:
        f_n_writer = csv.writer(test_w, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        f_n_writer.writerows(data)


def write_to_csv():
    create_cvs(get_data(name_file()))


if __name__ == "__main__":
    write_to_csv()
