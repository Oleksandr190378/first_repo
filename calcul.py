


a = int(input('Enter a: '))
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
    print('fncorrect operator')  
    exit(1)


#b =input("Enter b: ")


print(f"result is: {c}")


