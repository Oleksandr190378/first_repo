import sys

phone_dic = {}

def inner():
    st = input('Enter the command: ')
    res = st.split()+ [' '] + [' ']
    return res

def decorator(func):
    def wrapper_decorator(el):
        if el.isalpha():
            return func(el)
        else:
            print('TypeError')        
    return wrapper_decorator   

@decorator    
def phone(el:str):
    if el in phone_dic:
        print(f'the {el} has a {phone_dic[el]} number')
    else:
        print('The contact is not in the dictionary')      

def hello():
    print('How can I help you?')

def Error_Handler(func):
    def Inner_Function(el1, el2):
        if el1.isalpha() and el2.isdecimal():
            print('Done')
            return func(el1,el2)
        else:
            print(" wrong data types")
    return Inner_Function

@Error_Handler
def add(el1, el2):
    phone_dic.update({el1:el2})   
@Error_Handler
def change(el1, el2):
    if el1 in phone_dic:
        phone_dic[el1] = el2
    else:
        print('The contact is not the dictionary')    

def show():
    print(phone_dic) 

dic_func = {'hello': hello, 'add': add, 'change': change, 'phone': phone, 'show': show,
             'good bye': 0, 'exit': 0, 'close': 0}

def entry(arg):
        e = dic_func[arg]
        return e

def good_bye(x:str, y:str):
    return x + ' ' + y

def do_work():
    args = sys.argv
    args = args[1:] + [' '] + [' ']# First element of args is the file name
    ind = True
    while ind:
        if len(args) == 2:
            print('You have not passed any commands in!')
            args = inner()
        else:
            g = True
            for a in range(len(args)):
                args[a] = args[a].lower()
                if args[a] == 'good':
                    args[a] = good_bye(args[a], args[a+1])
                if args[a] in dic_func:
                    g = False
                    if args[a] in ['hello', 'show']:
                        y = entry(args[a])
                        y()
                        args = inner()
                        break
                    elif args[a] in ['good bye', 'exit','close']:
                        ind = False        
                    elif args[a] == 'phone':
                        y = entry(args[a])    
                        y(args[a+1])
                        args = inner() 
                        break   
                    elif args[a] in ['add', 'change']:
                        y = entry(args[a])
                        y(args[a+1], args[a+2])     
                        args = inner()
                        break   
            if g:    
                print('Unrecognized command')
                args = inner()
               
if __name__ == '__main__':
    do_work()



    
    



