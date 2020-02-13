def word_length(phrase):
    lst = phrase.split()
    lengths = list(map(len,lst))
    return lengths

ph = input("Enter any phrase : ")
print(
    word_length(ph)
)