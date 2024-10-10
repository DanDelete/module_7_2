from pprint import pprint


def custom_write(file_name, strings):
    file = open(str(file_name), 'r')
    file = open(str(file_name), 'w',encoding='utf-8')
    num = 0
    strok = 0

    for i in strings:
        strok = file.tell()
        num += 1
        file.write(f"{i}\n")
        print(((num, strok), f'{i}'))
    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
