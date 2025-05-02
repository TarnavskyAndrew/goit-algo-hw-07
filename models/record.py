from models.fields import Phone, Name, Birthday
# from colorama import Fore


# 4. Клас запису: описує один запис (контакт): ім'я + список телефонів
class Record: 
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        
    def add_phone(self, phone_str): #додає телефон                 
        self.phones.append(Phone(phone_str))      
        
    def remove_phone(self, phone_str): # видаляє телефон 
        phone = self.find_phone(phone_str)
        if phone:
            self.phones.remove(phone)
        else:
            # print(f"Phone '{phone_str}' not found.")
            return None                            
            
    def edit_phone(self, old, new): # замінює телефон, інакше `ValueError
        phone = self.find_phone(old)
        if phone:
            self.remove_phone(old)
            self.add_phone(new)
        else:
            raise ValueError(f"Phone number {old} not found.")           
        
    def find_phone(self, phone_str): #повертає `Phone` або None        
        for phone in self.phones:
            if phone.value == phone_str:
                return phone
        return None    
    
    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)    
    
    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"
