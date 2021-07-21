# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

texts = [b'class', b'function', b'method']

for bytes_text in texts:
    print(f"Содержимое переменной: {bytes_text}\n"
          f"Тип переменной:  {type(bytes_text)}\n"
          f"Длина переменной: {len(bytes_text)}\n")


