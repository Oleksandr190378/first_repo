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
         }



def directory_from_list(dir_path, dir_names): #extensions
    list_new_dir = []
    for folder in dir_names:
        if not os.path.exists(f'{dir_path}\\{folder}'):
            os.mkdir(f'{dir_path}\\{folder}')
        list_new_dir.append(f'{dir_path}\\{folder}')
    return list_new_dir

def get_file2(path, list_file): 
    for root, dirs, files in os.walk(path):
        
        list_file.append(files)  
    
    return list_file        
    
def get_folder(path, list_folder): # list_folder=[]
    for entry in os.scandir(path):  
        if not entry.is_dir(): 
            continue   
        else :
            t  = str(entry)
            t = t.removeprefix("<DirEntry \'")
            t = t.removesuffix("\'>")
            t.strip()            
            path2 = fr'{path}\{t}'  
            list_folder.append(path2) 
            get_folder(path2, list_folder)
    
    return list_folder


def get_file(path, list_file): # list_file=[]
    for entry in os.scandir(path):  
        if not entry.is_dir(): 
            t  = str(entry)
            t = t.removeprefix("<DirEntry \'")
            t = t.removesuffix("\'>")
            t = path + '\\' + t
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
    file_name = file_name.translate(TRANS)
    file_name = re.sub('\W', '_', file_name)
    
    return file_name


def sort_files(dir_path, extensions1):
    list_folder = get_folder(dir_path, [])
    file_list = get_file(dir_path, [])
    new_folder = {} 
    new_extensions = set()
    ext_unfound = set()
    ext_list = list(extensions1.items())
    
    list_new_dir = directory_from_list(dir_path, extensions1)
    for files in file_list:
        files2 = files.rsplit('.', 1)
        extension = files2[-1]
        file_name = files2[0]
        file_name2 = file_name.rsplit('\\', 1)
        file_name2 =file_name2[-1]
        file_name2 = normalize(file_name2)
        
        if extension in extensions1['archive']:
            shutil.unpack_archive(files, fr'{dir_path}\\archive\\{file_name2}')
            new_folder['archive'] = new_folder.get('archive', []) + [file_name2]
            new_extensions.add(extension)
            os.remove(files)
            continue
        ind = True
        new_file = file_name2 + '.' + extension
        
        for dict_key_int in range(len(ext_list)):
            
            if extension in ext_list[dict_key_int][1]:
                key1 = ext_list[dict_key_int][0]
                new_folder[key1]= new_folder.get(key1, []) + [new_file] #= new_folder[key1] + [new_file]
                shutil.move(files, fr'{dir_path}\\{ext_list[dict_key_int][0]}\\{new_file}')
                new_extensions.add(extension) 
                ind = False
                break 
        if ind == True:
             
            shutil.move(files, fr'{dir_path}\\{new_file}')
            ext_unfound.add(extension)
            
                
    
    list_folder.reverse()
    for p in list_folder:
       if p in list_new_dir:
           continue
       if  os.listdir(p) == []: 
            os.rmdir(p)   
    
    print(new_folder)
    print(new_extensions)
    print(ext_unfound)
    return new_folder , new_extensions, ext_unfound

#sort_files(main_path2, extensions1)

if __name__ == '__main__':
    
    if len(sys.argv) ==2:
        main_path =fr'{sys.argv[1]}'        
        if os.path.isdir(main_path):
            sort_files(main_path, extensions1)
        else:
            print(f'{main_path} is not a folder')
    else:
        print(f'Input a folder')        
    
    
    