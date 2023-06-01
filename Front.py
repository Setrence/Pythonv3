import datetime

import text_note_menu

def menu ():
    print(text_note_menu.main_menu)
    length_menu = len(text_note_menu.main_menu.split('\n')) - 1
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            return int(choice)
        else:
            print(f'Введите Число от 1 до {length_menu}')

def show_contact(telebook, error_message):
    if not telebook:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(telebook, 1):
            print(f'{contact.get("id"):<10}'
                  f'{contact.get("tail"):<10}'
                  f'{contact.get("body"):<10}'
                  f'{contact.get("date")}')
        return True

def add_contact():
    id = input('Введите ID: ')
    tail = input('Введите заголовок: ')
    body = input('Введите заметку: ')
    date = datetime.datetime.now()
    date = (str(date))
    return { 'id' : id, 'tail' : tail, 'body' : body, 'date' : date}

def indexx(message: str):
    return int(input(message))

def search(message):
    return input(message)

def change_contact(telebook: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, если нет изменений')
    contact = add_contact()
    return {'id': contact.get('id') if contact.get('id') else telebook[index - 1].get('id'),
            'tail': contact.get('tail') if contact.get('tail') else telebook[index - 1].get('tail'),
            'body': contact.get('body') if contact.get('body') else telebook[index - 1].get('body')}

def show_message(message):
    print('-' * len(message))
    print(message)
    print('-' * len(message))