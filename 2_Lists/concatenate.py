def concatenate(l1: list, l2: list, connector):
    return [word1 + connector + word2 for (word1, word2) in zip(l1, l2)]


print(concatenate(["a", "b", "c"], ["x", "y", "z"], "-"))
