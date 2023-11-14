'''initial_pin ='1234'

n = 0
while n < 3:

    user_pin = input('enter your pin: ' )

        if initial_pin == user_pin:
            
            amount = input('how much ')
            print(f'take your {amount}')
            break
        else :
            print('sorry. wrong pin ')

    else:
        print('pin should be 4 digits')  
    n = n+1

print('good buy')  '''

'''import random
number = random.randint(0,100)
tries = 0
while True:
    tries +=1
    if tries > 7:
        raise RuntimeError('You looser!!!')
    
    guess =input('what is a number?  ')
    if guess == 'exit':
        print('By by')
        break
    if  not guess.isnumeric() :
        print(f'Bad number {guess}!')
        continue
    
    int_guess = int(guess) 
    if  not 0<= int_guess <= 100 :
        print(f'Bad number {int_guess}!')
        continue 

    if int_guess > number:
        print('Too big')
    elif  int_guess < number:
        print('Too low ') 
    else:
        print('you win')
        break'''

'''base_rate = 40
price_per_km = 10
total_trip = 0


def calculate_trip_price(distance_km):
    global total_trip
    trip_price = base_rate + price_per_km*distance_km
    total_trip+=1
    return trip_price
    
print(calculate_trip_price(34))   
print(total_trip)'''

'''def get_fullname(first_name, last_name, middle_name=''):
    if middle_name =='':
       result = f'{first_name} {last_name}'
    else:
        result = f'{first_name} {middle_name} {last_name}'
    return result
        
resul = get_fullname('Petro', 'Zaliznyak')    
print(resul)'''

"""def mysum(*numbers):
    print(numbers)
    res = 0
    for i in numbers:
        res +=i
    return res

print(mysum(2,3,7,9,34,98))
def printsum(**argum):
    print(argum)  
    for key, value in argum.items():
        print(f'{key}: {mysum(*value)}')

printsum(first = [1, 3, 6], second = [45, 34, 23,23])    

ern = [2,56,23,78,456]
print(mysum(*ern))

www = {'q':[1,2,3], 'e':[1,2,3,4], 'v':[5,6,7]}
print(printsum(**www))
print(__name__)"""

'''def body(i):
    if i==3:
        return 'break'
    if i==2:
        return 'continue'
    print(i)

def body2(i):
    print(i+22)

def iterative( body_call, *your_list):
    for i in your_list:
        res = body_call(i)
        if res == 'break':
            break



def recursive(body_call, i=None, *your):
    if i != None:
        res =body_call(i)
        if res != 'break':
             recursive(body_call, *your)


def main():
    my = [1,23,3,48,5.67,6] 
    return recursive(body,*my)

 
#main()
if __name__ == '__main__' :   
    main()     '''

'''def amount_payment(payment):
    sum = 0
    for i in payment:
        if i> 0:
            sum = sum + i
    return sum   
    
n = [23, -34, 24, 23, 34, -34]   
print(amount_payment(n))    '''

'''def format_ingredients(items):
    if len(items) <=1:
        return items[0]
    else:
        a = items.pop(-1)
        items[-1] = items[-1] + ' and ' + a
        d = ', '.join(items)
        return d

print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]))'''

'''def get_grade(key):
    a = {'F': 1, 'FX': 2, "E": 3, 'D': 3, "C": 4, 'B': 5, 'A': 5}
    if a.get(key):

        return print(f'{key} == {a.get(key)}')
    

get_grade('') '''

'''def lookup_key(data, value):
    mylist = []
    for key, i in data.items():
        if value == i:
            mylist.append(key)

    return print(mylist)        

           
            

ddd = {2: 6, 'n': 9, 'g': 6, 8: 4, 'a': 9}

lookup_key(ddd, 9)   '''

'''def split_list(grade):
    
    list1 = []
    list2 = []
    if len(grade) == 0:
        return list1, list2
    
    d = sum(grade)/ len(grade)
    for i in grade:
        if i <= d:
            list1.append(i)
        else:
            list2.append(i) 
    return list1, list2           



g = []
nnn = (2, 3, 67, 3, 56, 12, 34, 12)    
print(split_list(g))'''

'''points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    sum = 0
    if len(coordinates) <= 1:
        return sum
    
    for t in range(len(coordinates)-1):
        h = coordinates[t]    
        k = coordinates[t+1]
        if h < k:
            sum = sum + points[(h,k)]
        elif h > k:
            sum = sum + points[(k,h)]   

    return print(sum)       


#calculate_distance([0, 1, 3, 2, 0, 3, 1 ])

my_list =['w', 4, 'e', 45, 'd', 34]
for w , r in enumerate(my_list):
    print(r, w)'''

'''def game(terra, power):
    power_sum = power
    for i in terra:
        for f in i:
            if f <= power_sum:
                power_sum+=f
            else:
                break
    return power_sum        
q = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]

e = [[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]]              
d = [[2, 4, 4, 3], [2 ,5 , 1], [1, 3, 2, 5]]
print(game(q, 1))'''

'''def is_valid_pin_codes(pin_codes):
    a = False   
    sas = set(pin_codes) 
    if len(pin_codes) ==len(sas):    
        for i in pin_codes:
            if len(i) == 4 and i.isnumeric():
                a = True 
            else:
                a = False
                return print(a)      
            
          
    return print(a)          
              

pun = []
pin = ['1101', '9934', '1191']          
is_valid_pin_codes(pin)  '''

'''from random import randint


def get_random_password():
    pin = ''
    while len(pin) < 8: 
        s = randint(40, 126)
        sign = chr(s)

        pin = pin + sign
    return pin


print(get_random_password())'''

'''def is_valid_password(password):
    r = False
    if len(password) == 8:
        
        for i in password:
            if  47<ord(i)<58:
                for j in password:
                    if  64<ord(j)<91:
                        for k in password:
                            if  96< ord(k)< 123:
                                r = True
     return print(r)  '''

'''def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return print(has_upper and has_lower and has_num)'''

'''def ss(a, e, s):
    if s > a*e:
        return False
    
    if s % a == 0 or s % e == 0:
        return True
    else:
        return False

        

print(ss(3, 3, 3))  '''

'''for i in range(12,1,-2):
    print(' '*i + "*"*(11-i))'''

'''from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num


def get_password():

    for i in range(0,100):   
        i +=1
        res = get_random_password()        
        if is_valid_password(res):
            return res
        
    

     
print(get_password())'''
'''sentence = 'heLLlo dear friSSend'

sen = sentence.split(' ')

for i in range(len(sen)):
    sen[i] = sen[i].lower()
    sen[i] = sen[i].title()

sen = ' '.join(sen)   '''

 

'''articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    articles_dict2 = []
    if letter_case == False:
        key = key.lower()
        for i in articles_dict:
            for k in i.values():            
                d = str(k).lower()
                if d.find(key) != -1:
                    articles_dict2.append(i)
                
    else:
        for i in articles_dict:
            for k in i.values():            
                d = str(k)
                if d.find(key) != -1:
                    articles_dict2.append(i)
                


    return articles_dict2            
key = 'Ark'


print(find_articles(key))'''

'''aa = '+38067+3800935 '
dd = [1, 2, 'w', 3, 4, 'q' ]
dd.extend([5, 7, 'a'])
def checkio(number: int) -> int:
    # your code here
    a = str(number)
    k = int(a[0])
    for i in a[1:]:
        if int(i) !=0:
            k = k*int(i)
        else:
            continue
    return k
    
def is_all_upper(text: str) -> bool:
    # your code here
    a = False
    if len(text) == 0 or text.isspace == True:
        a = True
    else:
        a = text.isupper()
    
    return a

print(is_all_upper("qAA SSS"))'''
              
'''def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    tot = {'UA':[], 'JP':[], "TW":[], 'SG':[]}
    for i in list_phones:
        i = sanitize_phone_number(i)
        if i.startswith('81'):
            tot['JP'].append(i)
        elif i.startswith('380'):
            tot ['UA'].append(i)   
        elif i.startswith('886'):
            tot ['TW'].append(i) 
        elif i.startswith('65'):
            tot ['SG'].append(i)       

    return tot

dd = ['81670000', '3803-333-3', '65222222']
print(get_phone_numbers_for_countries(dd))  
print(sanitize_phone_number('233-23-23')) '''

def is_spam_words(text, spam_words, space_around = False):
    text = text.lower()
    for i in spam_words:
        i = str(i).lower()
        if True == space_around :
            t = text.split(' ', '.')
            print(t)
            s = t.count(i)
            print(s)
            if s > 0:
                return True
        else:
            a =text.count(i)
            print(a)
            if a > 0:
                return True
    
    return False

#print(is_spam_words('Ты хорош, но выглядишь как лох.', ['лох'], True))        