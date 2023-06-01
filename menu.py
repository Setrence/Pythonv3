import Front
import Back
def start():
    Back.open_file()
    Front.show_message('Файл успешно открыт')
    while True:
        pb = Back.get_phone_book()
        choice = Front.menu()
        match choice:
            case 1:
                Back.save_file()
                Front.show_message('Файл успешно сохранен')
            case 2:
                Front.show_contact(pb, 'Заметки отсутствуют')
            case 3:
                Back.add_contact(Front.add_contact())
            case 4:
                if Front.show_contact(pb, 'Заметки отсутствуют'):
                    index = Front.indexx('Введите номер изменяемой заметки')
                    contact = Front.change_contact(pb, index)
                    Back.change_cont(contact, index)
                    Front.show_message(f'Заметка {Back.get_phone_book()[index - 1].get("name")} успешно изменена!')
            case 5:
                Front.show_contact(pb, 'Телефонная книга пуста или не открыта')
                index = Front.indexx('Введите номер удаляемой заметки: ')
                Back.dell_contact(pb, index)
                Front.show_message('Файл успешно удален')
            case 6:
                return


    # print('Выберите пункт меню:\n'
    #       '1) Вывести заметки на экран\n'
    #       '2) Добавить заметку\n'
    #       '3) Отредакттировкать заметку\n'
    #       '4) Удалить заметку\n'
    #       '5) Сохранить замеки\n')