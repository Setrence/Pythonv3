import datetime

import Back
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

def show_note(telebook, error_message):
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

def add_note(pb: list[dict]):
    count = int(pb[len(pb) - 1].get("id")) + 1
    id = str(count)
    print(f'ID вашей заметки: {id}')
    tail = input('Введите заголовок: ')
    body = input('Введите заметку: ')
    date = datetime.datetime.now()
    date = (str(date))
    print(show_message('Заметка успешно создана!'))
    return { 'id' : id, 'tail' : tail, 'body' : body, 'date' : date}

def indexx(message: str):
    return input(message)


def change_note(telebook: list[dict], id: str):
    index = 0
    for contact in telebook:
        index = index + 1
        if id in contact.get("id") and id != "":
            print('Введите новые данные или оставьте пустое поле, если нет изменений')
            contact = add_note(telebook)
            cont = {'id': telebook[index - 1].get('id'),
                    'tail': contact.get('tail') if contact.get('tail') else telebook[index - 1].get('tail'),
                    'body': contact.get('body') if contact.get('body') else telebook[index - 1].get('body'),
                    'date': contact.get('date') if contact.get('date') else telebook[index - 1].get('date')}
            Back.notes.pop(index - 1)
            Back.notes.insert(index - 1, cont)
            print(show_message('Заметка успешно изменена!'))
        elif index >= len(telebook):
            print(show_message('Введен неверный ID!'))
    return

def show_message(message):
    print('-' * len(message))
    print(message)
    print('-' * len(message))

