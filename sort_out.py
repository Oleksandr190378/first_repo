import re
import os
import shutil
main_path = r'C:\Users\user\Desktop\Dubai'

extensions = {

    'video': ['avi', 'mp4', 'mov', 'mkv'],

    'data': ['sql', 'sqlite', 'csv', 'dat', 'xml'],

    'audio': ['mp3', 'ogg', 'wav', 'amr'],

    'image': ['jpeg', 'png', 'jpg', 'svg'],

    'archive': ['zip', 'rar', 'gz', 'tar'],

    'text': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
    'other': []}


def directory_from_list(dir_path, dir_names):
    for folder in dir_names:
        if not os.path.exists(f'{dir_path}\\{folder}'):
            os.mkdir(f'{dir_path}\\{folder}')

def get_file2(path, directory):
    for root, dirs, files in os.walk(path):
        directory.append(files)
    return directory



def get_file(path, file):
    for entry in os.scandir(path):  
        if not entry.is_dir(): 
            t  = str(entry)
            t = t.removeprefix("<DirEntry \'")
            t = t.removesuffix("\'>")
            file.append(t)
            
        else :
            t  = str(entry)
            t = t.removeprefix("<DirEntry \'")
            t = t.removesuffix("\'>")
            t.strip() 
            path2 = fr'{path}\{t}'   
            get_file(path2, file)
    #take = set(file)
    return file

def normalize(file_name):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    Cyrillic =list(CYRILLIC_SYMBOLS)
    Cyrillic = tuple(Cyrillic)    
    TRANS = {}
    for c, l in zip(Cyrillic, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    file_name.translate(TRANS)
    file_name = re.sub('\W', '_', file_name)
    file_name = re.sub('\d', '_', file_name)
    return file_name
    



def sort_files(dir_path):
    file_list = list(get_file(dir_path, []))
    ext_list = list(extensions.items())

    for files in file_list:
        extension = files.rsplit('.', 1)[1]
        file_name = files.rsplit('.', 1)[0]
        normalize(file_name)
        new_file = file_name + '.' + extension

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                #print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                #os.rename(file_name, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')
                shutil.move(files, f'\\{ext_list[dict_key_int][0]}\{new_file}')
            else:
                #print(f'Moving {file_name} in {ext_list['other']} folder\n')
                shutil.move(files, f'\\{ext_list[dict_key_int]['other']}\{new_file}')








    
         
     


