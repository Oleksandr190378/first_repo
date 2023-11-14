import os
import re

def walk(pat, prev_dir):
    #os.getcwdb()
    os.chdir(pat) 
    listdir = list(filter(os.path.isdir, os.listdir(pat)))
    
    for el in listdir:
        listdir.remove(el)
        walk(fr'{pat}\{el}', listdir)
    



#pat = r'C:\Users\user\Desktop\Новая папка (3)\first_repo'
#print(os.listdir(r'C:\Users\user\Desktop\Новая папка (3)\first_repo'))
def total_salary(path):
    fh = open(path)
    suma = 0
    while True:        
        file = fh.readline()
        if not file:
            break
        numbers = file.rsplit(',', 1 )
        x = float(numbers[-1])        
        suma = suma +x        
    fh.close()
    return suma



def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    s = ''
    for i in employee_list:
        if type(i)==list:
            for k in i:
                s = s + k + '\n' 
        else:
            s = s + i + '\n'         
    fh.write(s)  
    fh.close()
    return s
d = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
def read_employees_from_file(path):
    list1 =[]
    fh = open(path, 'r')
    while True:
        line = fh.readline()
        if not line:
            break
        list1.append(line) 
        
    fh.close() 
    return list1
def get_cats_info(path):
    list_id = ['id', 'name', 'age']
    diction = []
    with open(path, 'r') as fh:
        while True:
            line = fh.readline()
            line = line.removesuffix('\n')
            if not line:
                break
            r = line.split(',')
            dic = {}
            for t in range(len(list_id)):
                dic[list_id[t]]= r[t]
            diction.append(dic)    

    return diction    

source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
line =''
for i in source:
    for t in i.values():
        line = line + str(t) + ','
    line = line.rstrip(',')  
    line += '\n'

print(line)









    
            