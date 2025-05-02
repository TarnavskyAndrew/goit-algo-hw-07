from collections import UserDict
from datetime import datetime
# from colorama import Fore

#  5. Адресна книга: зберігає всі записи
class AddressBook(UserDict): 
           
    def add_record(self, record): # додає телефон 
        self.data[record.name.value] = record
        
    def find(self, name): # повертає на ім'я 
        return self.data.get(name) 
    
    def delete(self, name): # видаляє на ім'я 
        
        if name in self.data:
            del self.data[name]
        else:                
            # print(f"Contact '{name}' not found.")
            return None  
        
    def show_all_contacts(self):
        return "\n".join(str(record) for record in self.data.values())    
    
    
    def get_upcoming_birthdays(self):
        today = datetime.today()
        upcoming = []
        for record in self.data.values():
            if record.birthday:
                bday = datetime.strptime(record.birthday.value, "%d.%m.%Y")
                bday_this_year = bday.replace(year=today.year)
                delta = (bday_this_year - today).days
                if 0 <= delta < 7:
                    upcoming.append(record)
        return upcoming        
    
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())