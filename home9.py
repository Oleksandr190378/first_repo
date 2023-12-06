import sys

phone_dic = {}

def inner():
    st = input('Enter the command: ')
    res = st.split() + [' '] + [' ']
    return res

def Input_Error(func):
    def Inner_Function(*el):
        try:
            el.index(' ') 
            return'Enter data after the command'
        except:
            try:
                return func(*el)
            except ValueError:
                return 'Please enter a valid name or number!' 
            except TypeError: 
                return 'The contact  is not in the dictionary'                       
    return Inner_Function

@Input_Error
def add(el1:str, el2:str):
    if el1.isalpha():
        if el2.isnumeric():
            phone_dic.update({el1:el2})
            return "Done"
        else:    
            raise ValueError
    else:
        raise ValueError       

@Input_Error
def change(el1:str, el2:str):
    if el1.isalpha():
        if el2.isnumeric():
            if el1 in phone_dic:
                phone_dic[el1] = el2
                return "Done" 
            else:
                raise TypeError   
        else:    
            raise ValueError
    else:
        raise ValueError

@Input_Error
def phone(el:str):
    if el.isalpha():
        if el in phone_dic:
            return phone_dic[el]
        else:
            raise TypeError   
    else:
        raise ValueError
    
def show():
    return phone_dic

dic_func = {'add': add, 'change': change, 'phone': phone, 'show': show,
             'good bye': 0, 'exit': 0, 'close': 0}

def entry(arg):
        e = dic_func[arg]
        return e

def good_bye(x:str, y:str):
    return x + ' ' + y

def do_work():
    args = sys.argv
    args = args[1:] + [' '] + [' '] # First element of args is the file name
    ind = True
    while ind:
        if len(args) == 2:
            print('You have not passed any commands in!')
            args = inner()
        else:
            g = True
            for a in range(len(args)):
                args[a] = args[a].lower()
                if args[a] == 'hello':
                    print('How can I help you?')
                    args = inner()
                    g = False
                    break
                if args[a] == 'good':
                    args[a] = good_bye(args[a], args[a+1])
                if args[a] in dic_func:
                    g = False
                    if args[a] == 'show':
                        y = entry(args[a])
                        print(y())
                        args = inner()
                        break
                    elif args[a] in ['good bye', 'exit','close']:
                        ind = False        
                    elif args[a] == 'phone':
                        y = entry(args[a])    
                        print(y(args[a+1]))
                        args = inner() 
                        break   
                    elif args[a] in ['add', 'change']:
                        y = entry(args[a])   
                        print(y(args[a+1], args[a+2]))
                        args = inner()
                        break                     
            if g:    
                print('Unrecognized command')
                args = inner()
               
if __name__ == '__main__':
    do_work()



   




    
    

    
    



