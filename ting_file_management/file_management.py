import os
import sys


def txt_importer(path_file):

    # Verifica se a extensão é .txt
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return []

    # Verifica se o arquivo existe
    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []

    with open(path_file, "r") as file:
        lines = file.read().split("\n")

    return lines
