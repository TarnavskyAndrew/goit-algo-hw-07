from datetime import datetime


# 1. Базовий клас для всіх полів запису
class Fields: 
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    
# 2. Клас імені - обов'язкове поле
class Name(Fields): 
    pass


# 3. Клас телефону з валідацією номера (10 цифр)
class Phone(Fields):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)  
        

# 4. Клас з датою народження, додає перевірку формату дати DD.MM.YYYY.
class Birthday(Fields):

    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")            