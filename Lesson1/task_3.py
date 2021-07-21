# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

texts = ['attribute', 'класс', 'type', 'функция']

for text in texts:
    try:
        print(f"Выражения '{text}' в байтовом формате: {text.encode('ascii')}")
    except UnicodeEncodeError:
        print(f"Выражение '{text}' не возможно передать в байтовом формате")
