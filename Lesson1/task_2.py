# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

texts = ['class', 'function', 'method']

for bytes_text in texts:
    print(f"Значение заносимое в переменную: '{bytes_text}'\n"
          f"Содержимое переменной в байтах: {bytes(bytes_text, 'utf-8')}\n"
          f"Тип переменной:  {type(bytes(bytes_text, 'utf-8'))}\n"
          f"Длина переменной: {len(bytes(bytes_text, 'utf-8'))}\n")


