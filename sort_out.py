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


def directory_from_list(dir_path, dir_names): #extensions
    for folder in dir_names:
        if not os.path.exists(f'{dir_path}\\{folder}'):
            os.mkdir(f'{dir_path}\\{folder}')

def get_file2(path, list_file): 
    for root, dirs, files in os.walk(path):
        list_file.append(files)

    return list_file

def get_folder(path, list_folder): 
    for root, dirs, files in os.walk(path):
        list_folder.append(dirs)
        
    return list_folder


def get_file(path, list_file): # list_file=[]
    for entry in os.scandir(path):  
        if not entry.is_dir(): 
            t  = str(entry)
            t = t.removeprefix("<DirEntry \'")
            t = t.removesuffix("\'>")
            list_file.append(t)
            
        else :
            t  = str(entry)
            t = t.removeprefix("<DirEntry \'")
            t = t.removesuffix("\'>")
            t.strip()
            path2 = fr'{path}\{t}'   
            get_file(path2, list_file)
    
    return list_file
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
    



def sort_files(dir_path, extensions):
    list_folder = get_folder(dir_path, [])
    file_list = get_file(dir_path, [])
    ext_list = list(extensions.items())
    directory_from_list(dir_path, extensions)
    for files in file_list:
        extension = files.rsplit('.', 1)[1]
        file_name = files.rsplit('.', 1)[0]
        normalize(file_name)
        new_file = file_name + '.' + extension

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
        
                shutil.move(files, f'\\{ext_list[dict_key_int][0]}\{new_file}')
            else:
                
                shutil.move(files, f'\\{ext_list[dict_key_int]['other']}\{new_file}')

    for new_file in os.scandir('\\archive\\') : 
        shutil.unpack_archive(new_file)
    
    for p in list_folder:
        if not os.listdir(p): 
            os.rmdir(p)   
    

    

def remove_dir (dir_path):
    list_folder = get_folder(dir_path, [])
    for p in list_folder:
        if not os.listdir(p): 
            os.rmdir(p)   








    
         
     


