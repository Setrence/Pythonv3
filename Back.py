import datetime

notes = []
def open_file ():
    with open('Notes.json', 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(';')
        contact = {'id' : fields[0], 'tail' : fields[1], 'body' : fields[2],  'date' : fields[3]}
        notes.append(contact)

def save_file ():
    data = []
    for contact in notes:
            data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open('Notes.json', 'w', encoding='UTF-8') as file:
        file.write(data)

def get_note_book():
    return notes

def add_note(contact):
    notes.append(contact)


def dell_note (notes, id):
    index = 0
    for contact in notes:
        index = index + 1
        if id in contact.get("id") and id != "":
            notes.pop(index - 1)
        elif index >= len(notes) or id == "":
            print("Заметки с таким id не существует")
            break