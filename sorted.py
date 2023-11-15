import re, sys
import os
import shutil

extensions1 = {

    'video': ['avi', 'mp4', 'mov', 'mkv'],

    'data': ['sql', 'sqlite', 'csv', 'dat', 'xml'],

    'audio': ['mp3', 'ogg', 'wav', 'amr'],

    'image': ['jpeg', 'png', 'jpg', 'svg'],

    'archive': ['zip', 'gz', 'tar'],

    'text': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    'other': []
         }



def directory_from_list(dir_path, dir_names): #extensions
    list_new_dir = []
    for folder in dir_names:
        d = os.path.join(dir_path, folder)
        if not os.path.exists(d):
            os.mkdir(d)
        list_new_dir.append(d)
    return list_new_dir

    
def get_folder(path, list_folder): # list_folder=[]
    
    for entry in os.listdir(path):  
        entry1 = os.path.join(path, entry)
        if not os.path.isdir(entry1):
            continue   
        else :
            list_folder.append(entry1)    
            path2 = os.path.join(path, entry) 
            get_folder(path2, list_folder)
    
    return list_folder

def get_file(path, list_file): # list_file=[]
    
    for entry in os.listdir(path):  
        entry1 = os.path.join(path, entry)
        if not os.path.isdir(entry1): 
            
            list_file.append(entry1)    
        else :
            path2 = os.path.join(path, entry)              
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
    file_name = file_name.translate(TRANS)
    file_name = re.sub('\W', '_', file_name)
    
    return file_name


def sort_files(dir_path, extensions1):
    list_folder = get_folder(dir_path, [])
    file_list = get_file(dir_path, [])
    new_folder = {} 
    new_extensions = set()
    ext_unfound = set()
    
    list_new_dir = directory_from_list(dir_path, extensions1)
    for files in file_list:
        files_list = os.path.splitext(files)
        files_list2 = os.path.split(files)
        extension = files_list[-1]
        
        file_name = files_list2[-1].split('.')
        file_name2 = file_name[0]
        extension2 = file_name[-1]
        extension3 = extension2.lower()
        file_name2 = normalize(file_name2)
        
        if extension3 in extensions1['archive']:
            des_path = os.path.join(dir_path, 'archive', file_name2)
            try:
                shutil.unpack_archive(files, des_path)
                new_folder['archive'] = new_folder.get('archive', []) + [file_name2]
                new_extensions.add(extension2)
                os.remove(files)
            except:
                shutil.move(files, des_path)
                new_extensions.add(extension2) 

            continue
        ind = True
        new_file = file_name2 +  extension
        for dict_key_int in extensions1.keys():
            if extension3 in extensions1[dict_key_int]:
                new_folder[dict_key_int] = new_folder.get(dict_key_int, []) + [new_file]
                des_path2 = os.path.join(dir_path, dict_key_int, new_file)
                shutil.move(files, des_path2)
                new_extensions.add(extension2) 
                ind = False
                break 

        
        if ind == True:
             
            shutil.move(files, os.path.join(dir_path, 'other',  new_file))
            new_folder['other'] = new_folder.get('other', []) + [new_file]
            ext_unfound.add(extension2)
            
                
    
    list_folder.reverse()
    for p in list_folder:
       if p in list_new_dir:
           continue
       if  os.listdir(p) == []: 
            os.rmdir(p)   
    
    print(f'Список файлів: {new_folder}')
    print(f'Відомі розширення: {new_extensions}')
    print(f'Невідомі розширення: {ext_unfound}')
    return new_folder , new_extensions, ext_unfound


if __name__ == '__main__':
    
    if len(sys.argv) ==2:
        main_path =fr'{sys.argv[1]}'        
        if os.path.isdir(main_path):
            sort_files(main_path, extensions1)
        else:
            print(f'{main_path} is not a folder')
    else:
        print(f'Input a folder')      
    
    
    