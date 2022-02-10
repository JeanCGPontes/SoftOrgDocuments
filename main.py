# Será usado para este programa o paradigma procedural.
# SoftOrgDocuments — Software de Organização de Documentos.
import os
import shutil

import functions

path = r"E:\Programação\Python\Projetos\SoftOrgDocuments\arquivo"

for file in os.listdir(path):
    file_directory = fr"{path}\{file}"
    file_type = functions.getFileType(file_directory)["classe"]

    if file_type is None:
        continue

    if not os.path.exists(fr"{path}\{file_type}"):
        print(fr"Criado {path}\{file_type}")
        os.makedirs(fr"{path}\{file_type}")
        print(fr"{file} -> {path}\{file_type}")
        shutil.move(src=file_directory, dst=fr"{path}\{file_type}\{file}")

    else:
        print(fr"{file} -> {path}\{file_type}")
        shutil.move(src=file_directory, dst=fr"{path}\{file_type}\{file}")


"print(functions.getDateImage(image_directory))"
