import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="selecione uma pasta")


lista_arquivos = os.listdir(caminho)


locais = {
    "imagens": [".png", ".jpg"],
    "pdfs" : [".pdf"],
    "Documento Word" : [".docx"],
    "Arquivo Executavel" : [".exe"],
    "Videos" : [".mp4"],
    "Power Point" : [".potx"],
    "Arquivo Photoshop" : [".psd"],
    "Textos não formatados" : [".txt"],
    "Arquivos compactados" : [".compactar"]    
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")    