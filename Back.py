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

def get_phone_book():
    return notes

def add_contact(contact):
    notes.append(contact)

# def change_cont (contact: list[dict], id: int):
#     index = 0
#     for value in contact:
#         index = index + 1
#         if value.get("id") == id:
#             break
#     notes.pop(index - 1)
#     notes.insert(index - 1, contact)

def dell_contact (notes, index):
    notes.pop(index - 1)

