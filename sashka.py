'''initial_pin ='1234'

n = 0
while n < 3:

    user_pin = input('enter your pin: ' )

    if len(user_pin) ==4 or len(user_pin) ==6:
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

import random
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
        break

