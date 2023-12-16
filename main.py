from collections import UserDict
from datetime import datetime, date, timedelta


class Field:
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    
    def __init__(self, value):
        self._value = None
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if value.isnumeric() and len(value) == 10:
            self._value = value  
        else:
            raise ValueError


class Birthday:
    
    def __init__(self, date):
        self._date = None
        self.date = date
        
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if  datetime.strptime(date, r"%d-%m-%Y"):
            self._date = date
        else:  
            raise ValueError      
       

class Record:
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        Phone(phone)
        self.phones.append(phone) 
        return self.phones    
    
    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)    
    
    def edit_phone(self, phone, new_phone): 
        Phone(new_phone)
        if phone in self.phones :
            ind = self.phones.index(phone)
            self.phones.insert(ind, new_phone)
            self.phones.remove(phone)
        else:
            raise ValueError    
    
    def find_phone(self, phone):
        if self.phones == []:
            return None
        else:
            if phone in self.phones:
                return Phone(phone) 
            else:
                return None
    
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


class Iterable:
   
    def __init__(self, max_points):
        self.current_point = 0
        self.max_points = max_points

    def __next__(self):
        if self.current_point < self.max_points:
            self.current_point +=1
            return    


class AddressBook(UserDict):
    
    def list_contacts(self):
        return list(self.data.keys())

    def add_record(self, object):
        contact = object.name.value
        self.data[contact] = object
        
      
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
            for el in list1[:N]:
                yield  el



