
from copy import copy, deepcopy
from pprint import pprint

num_2d = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8]
]

print(num_2d)
pprint(num_2d)
print(num_2d[1][2])
letters = ['a', 'b', 'c', 'd']
letters_2d = [copy(letters), copy(letters), copy(letters)]
letters_2d[1][0] = 'e'

pprint(letters_2d)
