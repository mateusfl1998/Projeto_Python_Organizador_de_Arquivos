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


def criando_pastas(diretorio):
    contador = 0
    for i in nomes_das_pastas:
        diretorio = f'/Users/MTec Celulares/Desktop/{nomes_das_pastas[contador]}'
        os.makedirs(diretorio)
        contador +=1

def move_archives():
    diretorio = os.listdir('/Users/MTec Celulares/Desktop')
    n = 0

    for i in diretorio:
        arquivo = f'/Users/MTec Celulares/Desktop/{diretorio[n]}'
        print(arquivo)
        n += 1
        if i[-4:] == '.zip' or i[-4:] =='.rar' or i[-3:] =='.7z':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos Rar')
        if i[-4:] == '.exe':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos EXECUTÁVEIS')
        if i[-4:] == '.jpg' or i[-4:] == '.png':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos JPG')
        if i[-4:] == '.pdf':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos PDF')
        if i[-5:] == '.html':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Para HTML')
        if i[-5:] == '.docx' or i[-4:] == '.txt':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos World e TXT')
        elif i != 'Organizador de Arquivos' or i != 'Pasta Para Pastas':
            pass

    