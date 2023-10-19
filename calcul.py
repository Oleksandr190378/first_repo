


'''a = int(input('Enter a: '))
b = int(input('Enter b: '))
oper =input('Enter operator: ')

if oper == "+":
    c = a + b
elif oper == "-":
    c = a-b
elif oper == "*":
    c = a*b
elif oper == "/":
    c = a/b
else :
    print('incorrect operator')  
    exit(1)


#b =input("Enter b: ")


print(f"result is: {c}")'''

'''num = int(input("Enter integer (0 for output): "))
sum = 0
sum2 = 0
while num != 0:
    num = num+1
    for i in range(num):
        sum = sum + i
        sum2 = sum + sum2  
    print(sum2)
    sum2 = 0
    sum = 0
    num = int(input("Enter integer (0 for output): "))'''

'''message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch == ' ' or ch == '!' :
        encoded_message = encoded_message + ch
    elif   ord(ch) > 96:
        i = ord(ch) - ord('a') 
        i = (i + offset) % 26
        encoded_message = encoded_message +  chr( i+ ord('a')) 
    else: 
         i = ord(ch) - ord('A') 
         i = (i + offset) % 26
         encoded_message = encoded_message +  chr( i+ ord('A'))     

print (encoded_message)'''

result = 0
wait_for_number = True

operand = int(input(" enter figure:  "))
operator = input( 'enter symbol: ')
while wait_for_number :
    if  operator =="+" or operator =="-" or operator =="/" or operator =="*" or operator == "=":
        wait_for_number = False
    else:
        print (' Invalid operator. try again ')
        operator = input(" enter symbol: ")    
        
result = operand
while operator != '=':    
    
    try:    
        operand = int(input( 'enter figure: '))  
        if operator == '-':
            result = result - operand
        elif operator == '+':
            result = operand + result
        elif operator == '*' :
            result = operand * result 
        elif operator == '/':
            result =  result / operand
        elif operator == '=':
            continue     
        else:
            print (' Invalid operator. try again ')
            operator = input(" enter symbol: ")
            continue
        print(result)
        operator = input(" enter symbol: ")
        if operator =="+" or operator =="-" or operator =="/" or operator =="*" or operator == "=":
            continue
        else :
            print (' Invalid operator. try again ')
            operator = input(" enter symbol: ")
         
    except  ValueError:
        print (' error number. try again ')
        
      
print(result)
