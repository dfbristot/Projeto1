"""
Projeto 1
Elaboração de organizador de arquivos com a utilização dos comandos os SHUTIL
Daniel Francisco Bristot
31/08/2022
Arquivo principal
"""
import utilitario
import os
import shutil

def main():
    arquivos = os.listdir()
    for diretorio in ['documentos','planilhas']:
        utilitario.criaFolder(diretorio)    
    utilitario.move_arquivos(arquivos)

if __name__ == "__main__":
    main()
