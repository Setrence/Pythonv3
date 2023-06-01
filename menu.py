import Front
import Back
def start():
    Back.open_file()
    Front.show_message('Файл успешно открыт')
    while True:
        pb = Back.get_note_book()
        choice = Front.menu()
        match choice:
            case 1:
                Back.save_file()
                Front.show_message('Файл успешно сохранен')
            case 2:
                Front.show_note(pb, 'Заметки отсутствуют')
            case 3:
                Back.add_note(Front.add_note(pb))
            case 4:
                if Front.show_note(pb, 'Заметки отсутствуют'):
                    id = Front.indexx('Введите id изменяемой заметки: ')
                    Front.change_note(pb, id)
            case 5:
                Front.show_note(pb, 'Телефонная книга пуста или не открыта')
                id = Front.indexx('Введите id удаляемой заметки: ')
                Back.dell_note(pb, id)
                Front.show_message('Заметка успешно удалена')
            case 6:
                break
