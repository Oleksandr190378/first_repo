


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
"""def check_operator(wait_for_number, operator ):
        while wait_for_number :
            if  operator =="+" or operator =="-" or operator =="/" or operator =="*" or operator == "=":
                wait_for_number = False
            else:
                print (' Invalid operator. try again ')
                operator = input("enter symbol: ")
                   
        return operator

result = 0

wait_for_number = True
operand = int(input(" enter figure:  "))
operator = input( 'enter symbol: ')

operator = check_operator(wait_for_number, operator)

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
        '''else:
            print (' Invalid operator. try again ')
            operator = input(" enter symbol: ")
            continue'''
        print(result)
        operator = input(" enter symbol: ")
        wait_for_number = True
        operator = check_operator(wait_for_number, operator)
         
    except  ValueError:
        print (' error number. try again ')
        
      
print(result)"""

'''from pathlib import Path
p = Path('/Desktop/Новая папка (3)/first_repo/sashka.py')

def parse_folder(path):
    
    files = []
    folders = []
    for a in path.iterdir():
        
        if a.is_dir():
            folders.append(a.name)
            items = a.glob('*.**')
            for item in items:
                files.append(item.name)
        else:
            files.append(a.name)
            
        
            
    return files, folders



print(parse_folder(p))'''

import sys

def main():
    d = sys.argv
    d.pop(0)
    d.append(' hello')
    d.append('world')
    result = ' '
    spl = result.join(d)
    
    print(spl)

n = '   hello darling, I am here!' 
t ='          *****'

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
vegs = ['cucumber', 'tomato', 'pepper']
dd = ['','']
newlist = [x for x in fruits  ]


x = int(input())
y = int(input())
z = int(input())
n = int(input())
s = [x, y, z]
s.insert(1, 'w')
c = [0, 0, 0]
new_list = [ c for  c in s if c != n]
'''for i in range(x+1):
    for a in range(y+1):
        for w in range(z+1):
            if i + a + w != n:
                g = [i, a, w]
                s.append(g)

print(s)'''


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
c=sum(student_marks[query_name])/len(student_marks[query_name])

print("%.2f" % round(c,2))