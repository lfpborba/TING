from ting_file_management.file_management import txt_importer
import os
import sys


def process(path_file, instance):
    file_content = txt_importer(path_file)
    queue_size = len(instance)

    if not file_content:
        return

    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }

    for file in range(queue_size):
        if instance.search(file)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(processed_data)
    print(processed_data)


def remove(queue):
    if not queue:
        print("Não há elementos")
    else:
        file = queue.dequeue()
        print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")


def file_metadata(queue, index):
    try:
        return print(queue.search(index), file=sys.stdout)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)