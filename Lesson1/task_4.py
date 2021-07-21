# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
# представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

texts = ['разработка', 'администрирование', 'protocol', 'standard']

for text in texts:
    encode_text = text.encode("utf-8")
    print(f"Выражение << {text} >> в закодированном виде: {encode_text}")
    print(f"Обратная кодировка << {encode_text.decode('utf-8')} >>")
