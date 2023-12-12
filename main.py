from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.value = self.valid_phone(value)
    
    def valid_phone(self, value):
        if value.isnumeric():
            if len(value) == 10:
                return value
            else:
                raise ValueError
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
        else:
            print(f'phone {phone} is not in a list')
    
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
    
    def get_phones(self):
        return self.phones
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"    


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
            print(f'Contact {contact} is not in address book')
        
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            print(f'Contact {name} is not in address book')  



