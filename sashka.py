initial_pin ='1234'

n = 0
while n < 3:

    user_pin = input('enter your pin: ' )

    if len(user_pin) ==4 or len(user_pin) ==6:
        if initial_pin == user_pin:
            print('pin is right')
            break
        else :
            print('sorry. wrong pin ')

    else:
        print('pin should be 4 digits')  
    n = n+1

print('good buy')          



