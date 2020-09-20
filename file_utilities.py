import shutil
import os
import re


def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:].lower()


def is_text_file(event):
    if extension_type(event) == 'txt':
        return True
    return False


def is_pdf_file(event):
    if extension_type(event) == 'pdf':
        return True
    return False


def is_mp3_file(event):
    if extension_type(event) == 'mp3':
        return True
    return False


def is_image_file(event):
    if extension_type(event) in ('png', 'jpg', 'bmp', 'gif', 'raw', 'svg', 'jpeg'):
        return True
    return False


def is_video_file(event):
    if extension_type(event) in ('mov', 'mp4', 'avi', 'flv'):
        return True
    return False


def is_doc_file(event):
    if extension_type(event) in ('doc', 'docx'):
        return True
    return False


def is_spreadsheet_file(event):
    if extension_type(event) in ('xls', 'xlsx'):
        return True
    return False


def is_presentation_file(event):
    if extension_type(event) in ('ppt', 'pptx'):
        return True
    return False


def is_code_file(event):
    if extension_type(event) in ('py', 'cs', 'js', 'php', 'html', 'sql', 'css'):
        return True
    return False


def is_executable_file(event):
    if extension_type(event) in ('exe', 'msi'):
        return True
    return False


def is_json_file(event):
    if extension_type(event) in ('json'):
        return True
    return False


def is_winrar_file(event):
    if extension_type(event) in ('zip', 'rar', 'iso'):
        return True
    return False


def deleted_copy(path):
  files = os.listdir(path)
  content_files = []  
  for file in files:
    try:      
      nameFile = re.findall(r'([\d\D+]+)(\(\d\)\.[a-z]+)', file)[0]
      if nameFile[0] in content_files:      
        os.remove(f'{path}\\{nameFile[0]}{nameFile[1]}')
      else:
        content_files.append(nameFile[0])
    except IndexError:
      pass
    except:
      print('Erro desconhecido')    
    


def make_folder(foldername):
    os.chdir('C:\\Users\\andre\\Downloads')
    if os.path.exists(foldername) == True:        
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
        deleted_copy(path_to_new_folder)        
    except:
        try:
            os.remove(event.src_path)        
        except:
            pass       
