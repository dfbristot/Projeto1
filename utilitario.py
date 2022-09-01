"""
Projeto 1
Elaboração de organizador de arquivos com a utilização dos comandos os SHUTIL
Daniel Francisco Bristot
31/08/2022
"""
import os
import shutil
#Primerio criar os diretorios na organizador
def criaFolder(nome_diretorio: str):
    if os.path.exists(nome_diretorio) == False:
        os.mkdir(nome_diretorio)

#Cria a função para mover os arquivos da pasta        
def move_arquivos(arquivos: list):
    for arquivo in arquivos:
        if ".xls" in arquivo:
            shutil.move(arquivo, f"./planilhas/{arquivo}")
        elif ".doc" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")