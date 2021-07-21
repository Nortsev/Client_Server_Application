'''Создать текстовый файл test_file.txt, заполнить его тремя строками: 
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл
в формате Unicode и вывести его содержимое'''



import locale
texts = ['сетевое программирование', 'сокет', 'декоратор']
with open("test_file.txt", 'w') as write:
    for text in texts:
        write.writelines(f'{text}\n')
write.close()
print(f'Кодировка по умолчанию: {locale.getpreferredencoding()}\n')

with open("test_file.txt", 'r', encoding='utf-8') as read:
    for line in read:
        print(line)
read.close()

