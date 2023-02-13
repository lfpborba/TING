from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue) -> list:
    case_insensitive_word = word.lower()
    words_list = []
    dict = {}
    lines = []

    for file in instance.queue:
        dict['palavra'] = case_insensitive_word
        dict['arquivo'] = file["nome_do_arquivo"]
        dict["ocorrencias"] = []

        for i, line in enumerate(file["linhas_do_arquivo"]):
            if case_insensitive_word in line.lower():
                word_events = {"linha": i + 1}
                lines.append(word_events)
                dict['ocorrencias'] = lines
        if dict["ocorrencias"]:
            words_list.append(dict)

    return words_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
