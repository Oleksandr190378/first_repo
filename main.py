from collections import UserDict
from datetime import datetime, date, timedelta


class Field:
    
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    def is_valid(self, value):
        return True

    @value.setter
    def value(self, value):
        if self.is_valid(value):
            self._value = value
    

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    
    def is_valid(self, value):
        if value.isnumeric() and len(value) == 10:
            self._value = value
            return True  
        else:
            raise ValueError


class Birthday(Field):
    
    def is_valid(self, value):
        if  datetime.strptime(value, r"%d-%m-%Y"):
            self._date = value
            return True
        else:  
            raise ValueError      
       

class Record:
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone) 
        return self.phones    
    
    def remove_phone(self, phone):
        for tel in self.phones:
            if tel.value == phone:
                self.phones.remove(tel)    
    
    def edit_phone(self, phone, new_phone): 
        for tel in self.phones:
            if tel.value == phone:
                new_phone = Phone(new_phone)
                ind = self.phones.index(tel)
                self.phones.insert(ind, new_phone)
                self.phones.remove(tel)
                break
            else:
                raise ValueError    
    
    def find_phone(self, phone):
        for tel in self.phones:
            if tel.value == phone:
                return tel
                    
    def days_to_birthday(self, birthday):
        t_date = date.today()
        birth = (datetime.strptime(birthday.date, r"%d-%m-%Y")).date()
        birth = birth.replace(year = t_date.year)
        if t_date <  birth:
            quantity = birth - t_date
        else:
            birth = birth.replace(year = t_date.year+1)
            quantity = birth - t_date
        return quantity.days

    def get_phones(self):
        return self.phones
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"    


class AddressBook(UserDict):
    
    def list_contacts(self):
        return list(self.data.keys())

    def add_record(self, record):
        contact = record.name.value
        self.data[contact] = record
        
      
    def find(self, contact):
        if contact in self.data:
            return self.data[contact] 
        else:
            return None
        
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            return None
        
    def iterator(self, N):
            list1 = list(self.data.items())
            yield list1[:N]


