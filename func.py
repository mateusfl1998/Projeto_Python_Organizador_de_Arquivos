import os
import shutil

nomes_das_pastas= [
    'Pasta Arquivos EXECUTÁVEIS',
    'Pasta Arquivos World e TXT',
    'Pasta Arquivos PDF',
    'Pasta Arquivos PNG',
    'Pasta Arquivos JPG',
    'Pasta Arquivos Torrent',
    'Pasta Arquivos Rar',
    'Pasta Para Pastas',
    'Pasta Para HTML'
]

""" Função para pegar o caminho da Área de Trabalho """
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")



def if_file_exist(file,folder):
    path = os.path.join(desktop_path, folder)
    path_archive_verify = os.path.join(desktop_path, folder,file)
    path_archive_delete = os.path.join(desktop_path,file)
    if os.path.exists(path_archive_verify):
        os.remove(path_archive_delete)
    else:
        shutil.move(path_archive_delete,path ) 

def criando_pastas():
    contador = 0
    for i in nomes_das_pastas:
        diretorio = f'{desktop_path}\{nomes_das_pastas[contador]}'
        print(diretorio)
        os.makedirs(diretorio)
        contador +=1

def move_archives():
    diretorio = os.listdir(desktop_path)
    n = 0

    for i in diretorio:
        if i[-4:] == '.zip' or i[-4:] =='.rar' or i[-3:] =='.7z':
            if_file_exist(i,'Pasta Arquivos Rar')
        if i[-4:] == '.exe':
            if_file_exist(i,'Pasta Arquivos EXECUTÁVEIS')
        if i[-4:] == '.jpg' or i[-4:] == '.png':
            if_file_exist(i,'Pasta Arquivos JPG')
        if i[-4:] == '.pdf':
            if_file_exist(i,'Pasta Arquivos PDF')
        if i[-5:] == '.html':
            if_file_exist(i,'Pasta Para HTML')
        if i[-5:] == '.docx' or i[-4:] == '.txt':
            if_file_exist(i,'Pasta Arquivos World e TXT')
        elif i != 'Organizador de Arquivos' or i != 'Pasta Para Pastas':
            pass

    