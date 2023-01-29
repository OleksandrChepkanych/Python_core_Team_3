import pickle
from datetime import datetime

class NoteBook:
    def __init__(self):
        self.datetimestr = str(datetime.now().strftime("%d%m%Y%H%M%S"))
        self.book = {}

    def __str__(self) -> str:
        return self.showall()
    
    def add(self, text: str, tag=""):
        self.text = text
        self.book[self.datetimestr] = [text, str(datetime.now().strftime("%d.%m.%Y %H:%M:%S")), tag]

    def delete(self, id: str):
        if self.book.__contains__(id):
            self.book.pop(id)
        else:
            return print("ID not found")

    def clear(self):
        self.book.clear()

    def edit(self, id, text, tag=""):
        if id in self.book:
            self.book[id][0] = text
        if tag:
            self.book[id][2] = tag

    def file_open(self):
        try:
            with open('NoteBook.txt', 'rb') as file_open:
                self.book = pickle.load(file_open)
        except OSError:
            return False
        return self.book

    def file_write(self):
        with open('NoteBook.txt', 'wb') as file_write:
            pickle.dump(self.book, file_write)

    def find(self, text: str) -> str:
        result = ""
        for id, record in self.book.items():
            if str(text).lower() in str(record[2]).lower():
                result += f"Tag: {record[2]}, ID: {id}, Date: {record[1]}\nText: {record[0]} \n\n"

        if not result:
            for id, record in self.book.items():
                if str(text).lower() in str(record[0]).lower():
                    result += f"Tag: {record[2]}, ID: {id}, Date: {record[1]}\nText: {record[0]} \n\n"
        if not result:
            return "Nothing found. Try something else"
        return result

    def showall(self) -> str:
        result = ""
        for id, record in self.book.items():
            result += f"Tag: {record[2]}, ID: {id}, Date: {record[1]}\nText: {record[0]} \n\n"
        if not result:
            return "Nothing found."
        return result

    def sortdate(self):
        #Сортування за датою
        sorted_values = sorted(self.book.keys())
        sorted_dict = {}
        for i in sorted_values[::-1]:
            sorted_dict[i] = self.book[i]
        result = ""
        for id, record in sorted_dict.items():
            result += f"Tag: {record[2]}, ID: {id}, Date: {record[1]}\nText: {record[0]} \n\n"
        if not result:
            return "Nothing found."
        return result

    def sortrag(self):
        #Сортування за тегами
        temp = {}
        rezult = ""
        for key, data in self.book.items():
            temp[key] = str(data[2])
        sorted_values = sorted(temp.values())

        for key in sorted_values:
            for n, data in temp.items():
                if data == key:
                    for id, record in self.book.items():
                        if id == n:
                            rezult += f"Tag: {record[2]}, ID: {id}, Date: {record[1]}\nText: {record[0]} \n\n"
        return rezult



text = NoteBook()
text.file_open()

while True:
    command_line = input('Input comand: ').split()
    command = command_line[0]
    if len(command_line) == 1:

        if command == "add":
            note = input('Input text for the note:\n')
            tag = input('Input tag for the note. Not necessarily:\n')
            text.add(note, tag)

        if command == "delete":
            id = input('Input ID for delete:\n')
            text.delete(id)
        
        if command == "edit":
            id = input('Input ID for edit:\n')
            note = input('Input NEU text for the note:\n')
            tag = input('Input NEU tag for the note. Not necessarily:\n')
            text.edit(id, note, tag)

        if command == "showall":
            print(text.showall())

        if command == "exit":
            text.file_write()
            print("Godbay")
            break
        
        if command == "save":
            text.file_write()
            print("The notebook is saved")
        
        if command == "sorted_date":
            print(text.sortdate())

        if command == "sorted_tag":
            print(text.sortrag())

        if command == "help":
            print("""
            'add' - to add a record\n
            'edit' - editing a record by ID\n
            'delete' - delete a record by ID\n
            'showall' - output of all records\n
            'save' - save changes\n
            'sorted_date' - sorting by date from newer records and output\n
            'sorted_tag' - sorting tags alphabetically and output\n
            'exit' - exit the program.
            """)

    else:
        print("Plis enter only comand. Command 'help' to view a list of commands")

