from ting_file_management.file_management import txt_importer

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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
