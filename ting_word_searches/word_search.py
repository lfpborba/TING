def exists_word(word, instance):
    search = []
    word = word.lower()

    for index in range(len(instance)):
        file = instance.search(index)

        ocurrences = [{"linha": i + 1}
                      for i, item in enumerate(file["linhas_do_arquivo"])
                      if word in item.lower()]

        if ocurrences:
            search.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": ocurrences
            })

    return search


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
