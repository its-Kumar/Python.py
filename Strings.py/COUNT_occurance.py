str = input("Enter any string : ")
lst = str.split()

for each_word in set(lst):
    print(each_word, " occurs ", lst.count(each_word), " times.")
