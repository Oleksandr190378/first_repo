import sys

phone_dic = {}

def inner():
    st = input('Enter the command: ')
    res = st.split()
    return res

def hello():
    print('How can I help you?')

def add(el1, el2):
    phone_dic.update({el1:el2})   
    print('Added')

def change(el1, el2):
    if el1 in phone_dic:
        phone_dic[el1] = el2
        print('Changed')
    else:
        print('The contact is not the dictionary')    
    
def phone(el):
    if el in phone_dic:
        print(f'the {el} has a {phone_dic[el]} number')
    else:
        print('The contact is not the dictionary')      

def show():
    print(phone_dic) 

dic_func = {'hello': hello, 'add': add, 'change': change, 'phone': phone, 'show': show,
             'good_bye': 0, 'exit': 0, 'false': 0}

def entry(arg):
        e = dic_func[arg]
        return e

def do_work():
    args = sys.argv
    args = args[1:] # First element of args is the file name
    ind = True
    while ind:
        if len(args) == 0:
            print('You have not passed any commands in!')
            args = inner()
        else:
            g = True
            for a in range(len(args)):
                args[a] = args[a].lower()
                if args[a] in dic_func:
                    g = False
                    if args[a] in ['hello', 'show']:
                        y = entry(args[a])
                        y()
                        args = inner()
                        break
                    elif args[a] in ['good_bye', 'exit', 'false']:
                        ind = False        
                    elif args[a] == 'phone':
                        try:
                            y = entry(args[a])    
                            y(args[a+1])
                        except:
                            print('ValueError')
                        args = inner() 
                        break   
                    elif args[a] in ['add', 'change']:
                        try:
                            if args[a+1].isalpha() and args[a+2].isdecimal():
                                y = entry(args[a])
                                y(args[a+1], args[a+2])   
                            else:
                                print('KeyError')    
                        except:
                            print('ValueError or KeyError')
                        args = inner()
                        break   
            if g:    
                print('Unrecognized command')
                args = inner()
               
if __name__ == '__main__':
    do_work()



    
    



