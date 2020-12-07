def filter_words(word_list, target_letter):
    return list(filter(lambda word: word.startswith(target_letter), word_list))


lst = [x for x in input("Enter words : ").split()]

print(filter_words(lst, "h"))
