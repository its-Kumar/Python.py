"""Given an array of strictly the characters 'R', 'G', and 'B', segregate the
values of the array so that all the Rs come first, the Gs come second, and the
Bs come last. You can only swap elements of the array. Do this in linear time
and in-place. For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G','G', 'B', 'B'].
"""


def swap_chars(input_):
    i = 0
    for j in range(1, len(input_)):
        if input_[j] == 'R' and input_[i] != 'R':
            input_[i], input_[j] = input_[j], input_[i]
            i += 1

    for j in range(i, len(input_)):
        if input_[j] == 'G' and input_[i] != 'G':
            input_[i], input_[j] = input_[j], input_[i]
            i += 1

    return input_


print(swap_chars(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
