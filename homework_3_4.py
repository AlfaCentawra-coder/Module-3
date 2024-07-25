def single_root_words(root_word, *other_words):
    root_word = root_word.upper()
    same_words = []
    list_other_words = list(other_words)
    for k in range (len(list_other_words)):
        list_other_words[k] = list_other_words[k].upper()
    for i in range (len(list_other_words)):
        if root_word in list_other_words[i] or list_other_words[i] in root_word:
            same_words.append(list_other_words[i])
    return print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')



